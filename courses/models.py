from django.db import models
from students.models import Student

class Course(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    duration_weeks=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(duration_weeks__gt=0), name='duration_positive')
        ]
    
    def get_student_count(self):
        return self.course_set.count()

    def can_delete(self):
        return self.get_student_count() == 0