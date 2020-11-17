# from django.db import models
# from djongo.models.fields import ArrayField
from djongo import models
from django import forms

# Create your models here.

class Error(models.Model):
    """
    Model for Error, identified by error_id (string),
    with attributes error_type (string), student_name (string),
    problem_number (string, corresponds with Problem object),
    assignment_id (string, corresponds with Assignment object),
    teacher_id (string, corresponds with Teacher object)
    """
    error_id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    problem_number = models.CharField(max_length=1003)
    assignment_id = models.CharField(max_length=1000)
    teacher_id = models.CharField(max_length=100)

class Problem(models.Model):
    """
    Model for Problem, identified by problem_number, 
    with array of errors.
    """
    problem_number = models.CharField(max_length=1003, primary_key = True)
    errors = models.ArrayField(
        model_container = Error
    )

class Assignment(models.Model):
    """
    Model for Assignment, identified by assignment_id (as string),
    with array of problems.
    """
    assignment_id = models.CharField(max_length=1000, primary_key = True)
    problems = models.ArrayField(
        model_container = Problem
    )

class Teacher(models.Model):
    """
    Model for Teacher, identified by teacher_id (as string), 
    with array of assignments.
    """
    teacher_id = models.CharField(max_length=100, primary_key = True)
    assignments = models.ArrayField(
        model_container = Assignment
    )