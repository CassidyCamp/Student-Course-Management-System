from django.urls import path
from .views import Enrollments, EnrollmentCreate

urlpatterns = [
    path('enrollments/', Enrollments.as_view(), name='enrollments'),
    path('enrollments/create/', EnrollmentCreate.as_view(), name='enrollment_create'),
]
