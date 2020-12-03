import graphene
from graphene_django import DjangoObjectType
from .models import Error, Problem, Assignment, Teacher
from .statistics import aggregate_errors, problem_errors, students_by_errors, type_of_errors
from graphene.types.generic import GenericScalar


# class StatisticType(graphene.ObjectType):
#     """
#     Object type for statistics that we are gathering
#     """
#
#     aggregate_errors = graphene.Int()
#     problem_errors = graphene.Int()
#     type_of_errors = graphene.JSONString()
#     students_by_errors = graphene.JSONString()
#
#     def resolve_aggregate_errors(parent, info):
#         return aggregate_errors(parent.parent)
#
#     def resolve_problem_errors(parent, info):
#         return problem_errors(parent.parent)
#
#     def resolve_type_of_errors(parent, info):
#         return type_of_errors(parent.parent)
#
#     def resolve_students_by_errors(parent, info):
#         return students_by_errors(parent.parent)


class ErrorType(DjangoObjectType):
    """
    Object Type for Errors from Hypatia.
    """

    class Meta:
        model = Error
        fields = ('error_id', 'error_type', 'student_name')
        filter_fields = ['error_id', 'error_type', 'student_name']

    error_type = graphene.String()

    def resolve_error_type(parent, info):
        return parent.error_type


class ProblemType(DjangoObjectType):
    """
    Object type for each problem in an assignment.
    """

    class Meta:
        model = Problem
        fields = ('problem_number',)
        filter_fields = ['problem_number']

    errors_below = graphene.List(ErrorType)

    def resolve_errors_below(parent, info):
        return parent.errors.all()


class AssignmentType(DjangoObjectType):
    """
    Object type for each Assignment
    """

    class Meta:
        model = Assignment
        fields = ('assignment_id',)
        filter_fields = ['assignment_id']

    # THIS MIGHT BECOME AN ISSUE
    problems_below = graphene.List(ProblemType)
    # statistic = graphene.Field(StatisticType)

    aggregate_errors = graphene.Int()
    problem_errors = GenericScalar()
    type_of_errors = GenericScalar()
    students_by_errors = GenericScalar()

    def resolve_problems_below(parent, info):
        return parent.problems.all()

    def resolve_aggregate_errors(parent, info):
        return aggregate_errors(parent)

    def resolve_problem_errors(parent, info):
        return problem_errors(parent)

    def resolve_type_of_errors(parent, info):
        return type_of_errors(parent)

    def resolve_students_by_errors(parent, info):
        return students_by_errors(parent)


class TeacherType(DjangoObjectType):
    """
    Object type for each Assignment
    """

    class Meta:
        model = Teacher
        fields = ('teacher_name',)
        filter_fields = ['teacher_name']

    assignments_below = graphene.List(AssignmentType)
    _id = graphene.String()

    def resolve_assignments_below(parent, info):
        return parent.assignments.all()

    def resolve_id(parent, info):
        return parent._id
