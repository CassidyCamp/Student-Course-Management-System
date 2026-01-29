from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpRequest, HttpResponse
from .models import Student
from enrollments.models import Enrollment
from django.utils import timezone
from django.db.models import Avg
from datetime import date

class Students(View):
    def get(slef, request: HttpRequest) -> HttpResponse:
        students = Student.objects.all()
        student = Student.objects.filter(age=16).first()
        
        avg_age = students.aggregate(avg=Avg("age"))["avg"]

        active_student = Student.objects.filter(
            student_set__isnull=False
        ).distinct().count()

        today = date.today()
        new_month = Student.objects.filter(
            created_at__year=today.year,
            created_at__month=today.month
        ).count()
        
        return render(request, 'students/student_list.html', context={
            "students": Student.objects.all(), 
            "avg_age": avg_age, 
            "enrolled_count": active_student, 
            "new_this_month": new_month,
        })
    

class StudentDetial(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        get_user = Student.objects.get(id=id)
        enrollments = Enrollment.objects.filter(student=get_user).select_related('course')
        return render(request, 'students/student_detail.html', context={"student": get_user,"enrollments": enrollments})
    
    
class StudentCreate(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'students/student_form.html')
    
    
    def post(self, request: HttpRequest) -> HttpResponse:
        print(request.POST)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        
        
        if Student.objects.filter(email=email).exists():
            return render(request, "students/student_form.html", {
                "error": "Bu email bilan student allaqachon mavjud"
            })
        
        if full_name and email and age:
            Student.objects.create(full_name=full_name, email=email, age=int(age))
            return redirect('/students/')
        
        
        
        return render(request, 'students/student_create.html', context={'error': 'Please fill all fields'})

class StudentDelete(View):
    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        student = get_object_or_404(Student, id=id)
        student.delete()
        return redirect('/students/')