from django.urls import path
from .views import Courses, CoursesDetail, CoursesCreate, CoursesEdit, CoursesDelet

urlpatterns = [
    path('courses/', Courses.as_view(), name='courses'),
    path('courses/<int:id>/', CoursesDetail.as_view(), name='course_detail'),
    path('courses/create/', CoursesCreate.as_view(), name='course_create'),
    path('courses/<int:id>/edit/', CoursesEdit.as_view(), name='course_edit'),
    path('courses/<int:id>/delete/', CoursesDelet.as_view(), name='course_delete'),
]
