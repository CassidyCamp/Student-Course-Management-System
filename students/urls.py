from django.urls import path
from .views import Students, StudentDetial, StudentCreate, StudentDelete

urlpatterns = [
    path('students/', Students.as_view(), name='students'),
    path('students/<int:id>/', StudentDetial.as_view(), name='student_detial'),
    path('students/create/', StudentCreate.as_view(), name='student_create'),
    path('students/<int:id>/delete/', StudentDelete.as_view(), name='student_delete'),
]
