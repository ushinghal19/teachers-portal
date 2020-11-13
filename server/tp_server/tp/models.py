from django.db import models

# Create your models here.

class Error(models.Model):
    error_id = models.CharField(max_length=1000, primary_key = True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)

class Problem(models.Model):
    problem_id = models.PositiveSmallIntegerField(primary_key = True)
    errors = models.ArrayField(
        model_container = Error
    )

class Assignment(models.Model):
    assignment_id = models.PositiveSmallIntegerField(primary_key = True)
    questions = models.ArrayField(
        model_container = Problem
    )

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100, primary_key = True)
    assignments = models.ArrayField(
        model_container = Assignment
    )
