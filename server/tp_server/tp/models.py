from django.db import models
from djongo.models.fields import ArrayField

# Create your models here.

class Error(models.Model):
    id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)


class Problem(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    errors = ArrayField(
        model_container=Error
    )


class Assignment(models.Model):
    assignment_id = models.PositiveSmallIntegerField(primary_key = True)
    problems = ArrayField(
        model_container=Problem
    )


class Teacher(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    assignments = ArrayField(
        model_container=Assignment
    )
