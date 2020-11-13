from django.db import models

# Create your models here.

class Error(models.Model):
    error_id = models.CharField(max_length=1000)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)

class Question(models.Model):
    question_number = models.PositiveSmallIntegerField()
    errors = models.ArrayField(
        model_container = Error
    )

class Assignment(models.Model):
    assignment_id = models.PositiveSmallIntegerField()
    questions = models.ArrayField(
        model_container = Question
    )

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100)
    assignments = models.ArrayField(
        model_container = Assignment
    )
