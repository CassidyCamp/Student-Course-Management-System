from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=16), name='age_gte_16')
        ]
