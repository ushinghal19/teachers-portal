# from django.db import models
# from djongo.models.fields import ArrayField
from djongo import models

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

    @staticmethod
    def create(errorID: str, errorType: str, studentName: str, \
                problemNumber: int, assignmentID: str, teacherID: str):
        """
        USE THIS TO CREATE ERROR
        Method to create Error with attributes:
        errorID (str): primary key
        errorType (str)
        studentName (str)
        problemNumber (int)
        assignmentID (str)
        teacherID (str)
        This will instantiate a Problem, Assignment, and Teacher if they do not exist.
        If Error exists already, do nothing.
        """
        if Error.objects.filter(error_id = errorID).count() == 0:
            error = Error()
            error.error_id = errorID
            error.error_type = errorType
            error.student_name = studentName
            error.problem_number = assignmentID + "_" + str(problemNumber)
            error.assignment_id = assignmentID
            error.teacher_id = teacherID
            error.save()
            Teacher.create(teacherID)
            Assignment.create(assignmentID, teacherID)
            Problem.create(problemNumber, assignmentID)
            problem = Problem.objects.get(problem_number = error.problem_number)
            problem.errors.append(error)
            problem.save()


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
    def create(problemNumber: int, assignmentID: str):
        """
        USE THIS TO CREATE PROBLEM
        Method to create problem, identified with problemNumber argument.
        Prerequisite: assignmentID must be an existing assignment_id in Assignment.
        Initializes with empty errors array.
        If Problem exists already, do nothing.
        """
        problem_str = assignmentID + "_" + str(problemNumber)
        if Problem.objects.filter(problem_number = problem_str).count() == 0:
            errors_array = []
            problem = Problem()
            problem.problem_number = problem_str
            problem.errors = errors_array
            problem.save()
            assignment = Assignment.objects.get(assignment_id = assignmentID)
            assignment.problems.append(problem)
            assignment.save()


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
    def create(assignmentID: str, teacherName: str):
        """
        USE THIS TO CREATE ASSIGNMENT
        Method to create assignment, identified with assignmentID argument.
        Prerequisite: teacherName must be an existing teacher name in Teachers.
        Initializes with empty problems array.
        If Assignment exists already, do nothing.
        """
        if Assignment.objects.filter(assignment_id = assignmentID).count() == 0:
            problems_array = []
            assignment = Assignment()
            assignment.assignment_id = assignmentID
            assignment.problems = problems_array
            assignment.save()
            teacher = Teacher.objects.get(teacher_name = teacherName)
            teacher.assignments.append(assignment)
            teacher.save()


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
    def create(teacherName: str):
        """
        USE THIS TO CREATE TEACHER OBJECT
        Method to create Teacher, identified with teacherName argument,
        initialized with an empty assignments array.
        If Teacher with teacherName exists already, do nothing.
        """
        if Teacher.objects.filter(teacher_name = teacherName).count() == 0:
            assignments_array = []
            teacher = Teacher()
            teacher.assignments = assignments_array
            teacher.teacher_name = teacherName
            teacher.save()