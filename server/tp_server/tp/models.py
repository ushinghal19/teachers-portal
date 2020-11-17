# from django.db import models
# from djongo.models.fields import ArrayField
from djongo import models
from django import forms

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100, primary_key = True)
    assignments = models.ArrayField(
        # holds assignment_id
        model_container = models.CharField(max_length=1000)
    )

class Assignment(models.Model):
    assignment_id = models.CharField(max_length=1000, primary_key = True)
    problems = models.ArrayField(
        # holds problem_number
        model_container = models.CharField(max_length=1003)
    )

class Problem(models.Model):
    problem_number = models.CharField(max_length=1003, primary_key = True)
    errors = models.ArrayField(
        # holds error_id
        model_container = models.CharField(max_length=1000)
    )

class Error(models.Model):
    error_id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    problem_number = models.ForeignKey(Problem, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)