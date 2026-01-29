from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest
from students.models import Student
from courses.models import Course
from django.utils import timezone

from .models import Enrollment


class Enrollments(View):
    def get(slef, request: HttpRequest) -> HttpResponse:
        enrollments = Enrollment.objects.all()
        
        active_courses = Course.objects.count()
        active_students = Student.objects.count()
        
        today = timezone.now().date()
        today_enrollments = Enrollment.objects.filter(
            enrolled_at__date=today
        ).count()

        return render(request, 'enrollments/enrollment_list.html', {
            'enrollments': enrollments,
            'active_courses': active_courses,
            'active_students': active_students,
            'today_enrollments': today_enrollments,
        })

class EnrollmentCreate(View):
    def get(slef, request: HttpRequest) -> HttpResponse:
        students = Student.objects.all()
        courses = Course.objects.all()


        return render(request, 'enrollments/enrollment_form.html', {
            'students': students,
            'courses': courses,
        })

    def post(slef, request: HttpRequest) -> HttpResponse:
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')

        Enrollment.objects.create(
            student_id=student_id,
            course_id=course_id
        )

        return redirect('enrollments')
