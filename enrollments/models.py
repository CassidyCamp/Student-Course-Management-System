from django.db import models
from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_set')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='course_set')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')
