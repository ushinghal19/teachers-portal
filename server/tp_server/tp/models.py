# from django.db import models
# from djongo.models.fields import ArrayField
from djongo import models

# Create your models here.


class Error(models.Model):
    """
    Model for Error, identified by error_id (string),
    with attributes error_type (string), student_name (string),
    problem_number (string, corresponds with Problem object),
    assignment_id (string, corresponds with Assignment object)
    """
    error_id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    problem_number = models.CharField(max_length=1003)
    assignment_id = models.CharField(max_length=1000)

    @staticmethod
    def create(error_id: str, error_type: str, student_name: str, \
               problem_number: int, assignment_id: str):
        """
        USE THIS TO CREATE ERROR
        Method to create Error with attributes:
        error_id (str): primary key
        error_type (str)
        student_name (str)
        problem_number (int)
        assignment_id (str)
        This will instantiate a Problem, Assignment, and Teacher if they do not exist.
        If Error exists already, raise error.
        """
        if Error.objects.filter(error_id = error_id).count() == 0:
            error = Error()
            error.error_id = error_id
            error.error_type = error_type
            error.student_name = student_name
            error.problem_number = assignment_id + "_" + str(problem_number)
            error.assignment_id = assignment_id
            error.save()
            problem = Problem.objects.get(problem_number = error.problem_number)
            problem.errors.append(error)
            problem.save()
            return error
        raise KeyError("An error with this ID has already been created")

class Problem(models.Model):
    """
    Model for Problem, identified by problem_number, 
    with array of errors.
    """
    problem_number = models.CharField(max_length=1003, primary_key = True)
    errors = models.ArrayField(
        model_container = Error
    )

    @staticmethod
    def create(problem_number: int, assignment_id: str):
        """
        USE THIS TO CREATE PROBLEM
        Method to create problem, identified with problem_number argument.
        Prerequisite: assignment_id must be an existing assignment_id in Assignment.
        Initializes with empty errors array.
        If Problem exists already, raise error.
        """
        problem_str = assignment_id + "_" + str(problem_number)
        if Problem.objects.filter(problem_number = problem_str).count() == 0:
            errors_array = []
            problem = Problem()
            problem.problem_number = problem_str
            problem.errors = errors_array
            problem.save()
            assignment = Assignment.objects.get(assignment_id = assignment_id)
            assignment.problems.append(problem)
            assignment.save()
            return problem
        raise KeyError("A problem with this ID already exists")

class Assignment(models.Model):
    """
    Model for Assignment, identified by assignment_id (as string),
    with array of problems.
    """
    assignment_id = models.CharField(max_length=1000, primary_key = True)
    problems = models.ArrayField(
        model_container = Problem
    )

    @staticmethod
    def create(assignment_id: str, teacher_name: str):
        """
        USE THIS TO CREATE ASSIGNMENT
        Method to create assignment, identified with assignment_id argument.
        Prerequisite: teacher_name must be an existing teacher name in Teachers.
        Initializes with empty problems array.
        If Assignment exists already, raise error.
        """
        if Assignment.objects.filter(assignment_id = assignment_id).count() == 0:
            problems_array = []
            assignment = Assignment()
            assignment.assignment_id = assignment_id
            assignment.problems = problems_array
            assignment.save()
            teacher = Teacher.objects.get(teacher_name = teacher_name)
            teacher.assignments.append(assignment)
            teacher.save()
            return assignment
        raise KeyError("An assignment with this ID already exists")

class Teacher(models.Model):
    """
    Model for Teacher, identified by teacher_id (as string), 
    with array of assignments.
    """
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    assignments = models.ArrayField(
        model_container = Assignment
    )

    @staticmethod
    def create(teacher_name: str):
        """
        USE THIS TO CREATE TEACHER OBJECT
        Method to create Teacher, identified with teacher_name argument,
        initialized with an empty assignments array.
        If Teacher with teacher_name exists already, raise error.
        """
        if Teacher.objects.filter(teacher_name = teacher_name).count() == 0:
            assignments_array = []
            teacher = Teacher()
            teacher.assignments = assignments_array
            teacher.teacher_name = teacher_name
            teacher.save()
        rasie KeyError("A teacher with this name already exists")