from django.shortcuts import render, redirect
from django.views import View
from .models import Course
from enrollments.models import Enrollment
from django.http import HttpResponse, HttpRequest
from django.db.models import Avg
from enrollments.models import Enrollment



class Courses(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        try:
            courses = Course.objects.all()
            for course in courses:
                course.student_count = course.get_student_count()
        except:
            return render(request, 'courses/course_list.html', context={"errors": "Hatolik yuzberdi"})


        active_courses = Course.objects.count()

        return render(request, 'courses/course_list.html', context={
            "courses": courses,
            "total_students": Enrollment.objects.count(),
            "avg_duration": round(courses.aggregate(Avg("duration_weeks"))["duration_weeks__avg"] or 0),
        })
        

class CoursesDetail(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        try:
            get_course = Course.objects.get(id=id)
            enrollments = Enrollment.objects.filter(course=get_course)
        except:
            return HttpResponse('yoq 02')
        
        return render(request, 'courses/course_detail.html', context={"course":get_course,"enrollments":enrollments})
     
    
class CoursesCreate(View):
    def get(slef, request: HttpRequest) -> HttpResponse:
        return render(request, 'courses/course_form.html')
    
    def post(self, request: HttpRequest) -> HttpResponse:
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration_weeks = request.POST.get('duration_weeks')
        
        new_course = Course(title=title, description=description, duration_weeks=duration_weeks)
        new_course.save()
        return redirect('courses')


class CoursesEdit(View):
    def get(slef, request: HttpRequest, id: int) -> HttpResponse:
        try:
            get_course = Course.objects.get(id=id)
        except:
            return HttpResponse('yoq 02')
        
        return render(request, 'courses/course_form.html', {"course": get_course})
    
    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration_weeks = request.POST.get('duration_weeks')
        
        get_course = Course.objects.get(id=id)
        get_course.title = title
        get_course.description = description
        get_course.duration_weeks = duration_weeks
        get_course.save()
        return redirect('courses')
    

class CoursesDelet(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        return redirect('courses')
    
    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        get_course = Course.objects.get(id=id)
        get_course.delete()
        return redirect('courses')