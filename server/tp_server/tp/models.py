from django.db import models
from djongo.models.fields import ArrayField

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100, primary_key = True)
    assignments = models.ArrayField(
        model_container = Assignment
    )

class Assignment(models.Model):
    assignment_id = models.CharField(max_length=1000, primary_key = True)
    problems = models.ArrayField(
        model_container = Problem
    )

class Problem(models.Model):
    problem_id = models.PositiveSmallIntegerField(primary_key = True)
    errors = models.ArrayField(
        model_container = Error
    )

class Error(models.Model):
    error_id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    problem_number = models.ForeignKey(Problem, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    teacher_id = models.ForeginKey(Teacher, on_delete=models.CASCADE)