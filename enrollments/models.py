from django.db import models
from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    enrolled_at = models.DateTimeField()

    class Meta:
        unique_together = ('student', 'course')
