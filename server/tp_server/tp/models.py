from bson import ObjectId
from djongo import models


class Error(models.Model):
    """
    Model for Error, identified by error_id (string),
    with attributes error_type (string), student_name (string).
    """
    error_id = models.CharField(max_length=1000, primary_key=True)
    error_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)

    objects = models.DjongoManager()

    @staticmethod
    def create(error_id: str, error_type: str, student_name: str, problem_number: int,
               assignment_id: str):
        """
        USE THIS TO CREATE ERROR
        Method to create Error with attributes:
        error_id (str): primary key
        error_type (sr)
        student_name (str)
        problem_number (int)
        assignment_id (str)
        This will instantiate a Problem and put it in the corresponding Assignment.
        """

        # TODO: Can we make some of these fields not mandatory? And then the same in the Schema.
        if not Error.objects.filter(error_id=error_id):
            error = Error()
            error.error_id = error_id
            error.error_type = error_type
            error.student_name = student_name

            try:
                problem = Problem.objects.\
                    get(problem_number=Problem.format_problem_id(problem_number, assignment_id))

            except Problem.DoesNotExist:
                problem = Problem.create(problem_number=problem_number,
                                         assignment_id=assignment_id)

            problem.errors.add(error)
            error.save()
            problem.save()
            return error

        raise KeyError("An error with this ID has already been created")


class Problem(models.Model):
    """
    Model for Problem, identified by problem_number,
    with array of errors.
    """
    problem_number = models.CharField(max_length=1003, primary_key=True)
    errors = models.ArrayReferenceField(
        to=Error,
        on_delete=models.CASCADE,

    )

    objects = models.DjongoManager()

    @staticmethod
    def format_problem_id(problem_number: int, assignment_id: str) -> str:
        return assignment_id + "_" + str(problem_number)

    @staticmethod
    def create(problem_number: int, assignment_id: str):
        """
        USE THIS TO CREATE PROBLEM
        Method to create problem, identified with problem_number argument.
        Prerequisite: assignment_id must be an existing assignment_id in Assignment.
        Initializes with empty errors array.
        If Problem exists already, raise error.
        """
        problem_str = Problem.format_problem_id(problem_number, assignment_id)
        if not Problem.objects.filter(problem_number=problem_str).exists():
            problem = Problem(problem_number=problem_str)

            try:
                assignment = Assignment.objects.get(assignment_id=assignment_id)

            except Assignment.DoesNotExist:
                raise KeyError(f"The assignment with the ID \
                {assignment_id} specified does not exist.")

            assignment.problems.add(problem)
            problem.save()
            return problem

        raise KeyError("A problem with this ID already exists")


class Assignment(models.Model):
    """
    Model for Assignment, identified by assignment_id (as string),
    with array of problems.
    """
    assignment_id = models.CharField(max_length=1000, primary_key=True)
    assignment_name = models.CharField(max_length=100, default="")
    problems = models.ArrayReferenceField(
        to=Problem,
        on_delete=models.CASCADE
    )
    objects = models.DjongoManager()

    @staticmethod
    def create(assignment_id: str, teacher_id: str, assignment_name: str):
        """
        USE THIS TO CREATE ASSIGNMENT
        Method to create assignment, identified with assignment_id argument.
        Prerequisite: teacher_id must be an existing teacher name in Teachers.
        Initializes with empty problems array.
        If Assignment exists already, raise error.
        """
        if not Assignment.objects.filter(assignment_id=assignment_id):
            assignment = Assignment(assignment_id=assignment_id, assignment_name=assignment_name)

            try:
                teacher = Teacher.objects.get(_id=ObjectId(teacher_id))

            except Teacher.DoesNotExist:
                raise KeyError(f"The teacher with the ID {teacher_id} specified does not exist.")

            teacher.assignments.add(assignment)
            assignment.save()
            return assignment

        raise KeyError("An assignment with this ID already exists")


class Teacher(models.Model):
    """
    Model for Teacher, identified by _id (as string),
    with array of assignments.
    """
    _id = models.ObjectIdField()
    teacher_name = models.CharField(max_length=100)
    assignments = models.ArrayReferenceField(
        to=Assignment,
        on_delete=models.CASCADE
    )
    objects = models.DjongoManager()

    @staticmethod
    def create(teacher_name: str):
        """
        USE THIS TO CREATE TEACHER OBJECT
        Method to create Teacher, identified with teacher_id argument,
        initialized with an empty assignments array.
        If Teacher with teacher_id exists already, raise error.
        """
        teacher = Teacher(teacher_name=teacher_name)
        teacher.save()
        return teacher
