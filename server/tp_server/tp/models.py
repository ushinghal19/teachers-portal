from django.db import models
from djongo.models.fields import ArrayField

# Create your models here.

class Error(models.Model):
    id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    problem_number = models.PositiveSmallIntegerField()
    assignment_id = models.PositiveSmallIntegerField()
    teacher_id = models.CharField(max_length=100)
