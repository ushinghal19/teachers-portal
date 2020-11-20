import graphene
from .object_types import ErrorType, ProblemType, AssignmentType, TeacherType
from .models import Error, Problem, Assignment, Teacher


class ErrorMutationCreate(graphene.Mutation):
    """
    Mutation for Errors from Hypatia.
    """

    class Arguments:
        error_id = graphene.String()
        error_type = graphene.String()
        student_name = graphene.String()
        problem_number = graphene.Int()
        assignment_id = graphene.String()

    error = graphene.Field(ErrorType)

    @classmethod
    def mutate(cls, root, info, error_id: str, error_type: str, student_name: str,
               problem_number: int,
               assignment_id: str):
        """
        Takes optional additional Error fields and creates a new error.
        """
        error = Error.create(error_id=error_id, error_type=error_type, student_name=student_name,
                             problem_number=problem_number, assignment_id=assignment_id)

        return cls(error=error)


class ProblemMutationCreate(graphene.Mutation):
    """
    Mutation for problems from Hypatia.
    """

    class Arguments:
        problem_number = graphene.Int()
        assignment_id = graphene.String()

    problem = graphene.Field(ProblemType)

    @classmethod
    def mutate(cls, root, info, problem_number: int, assignment_id: str):
        """
        Takes optional additional Error fields and creates a new problem.
        """

        problem = Problem.create(problem_number=problem_number, assignment_id=assignment_id)
        # problem.save()
        return cls(problem=problem)


class AssignmentMutationCreate(graphene.Mutation):
    """
    Mutation for problems from Hypatia.
    """

    class Arguments:
        assignment_id = graphene.String()
        teacher_id = graphene.String()

    assignment = graphene.Field(AssignmentType)

    @classmethod
    def mutate(cls, root, info, assignment_id: str, teacher_id: str):
        """
        Takes optional additional Error fields and creates a new problem.
        """
        assignment = Assignment.create(assignment_id=assignment_id, teacher_id=teacher_id)
        return cls(assignment=assignment)


class TeacherMutationCreate(graphene.Mutation):
    """
    Mutation for problems from Hypatia.
    """

    class Arguments:
        teacher_name = graphene.String()

    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, root, info, teacher_name: str):
        """
        Takes optional additional Error fields and creates a new problem.
        """
        teacher = Teacher.create(teacher_name=teacher_name)
        return cls(teacher=teacher)


# NOT TESTED OR UPDATED FOR NEW MODELS
#
# class HypatiaErrorMutationWithID(graphene.Mutation):
#     """
#     Mutation for Errors from Hypatia, when you specify an ID (from the Hypatia Companion App).
#     """
#
#     class Arguments:
#         id = graphene.String()
#         error_type = graphene.String()
#         student_name = graphene.String()
#
#     error = graphene.Field(HypatiaErrorType)
#
#     @classmethod
#     def mutate(cls, root, info, id: str, **kwargs):
#         """
#         Requires an ID method. Takes optional additional Error fields, and either updates
#         or creates the required field.
#         """
#         error, created = Error.objects.update_or_create(pk=id,
#                                                         defaults=kwargs)
#         return cls(error=error)
#
#
# class HypatiaErrorUpdate(HypatiaErrorMutationWithID):
#     """
#     Updates specified fields for Hypatia Errors from Hypatia, when you specify an ID.
#     """
#
#     @classmethod
#     def mutate(cls, root, info, id: str, **kwargs):
#         """
#         Requires an ID method. Takes optional additional Error fields and performs update.
#         """
#         error = Error.objects.get(pk=id)
#         if kwargs.get("error_type"):
#             error.error_type = kwargs.get("error_type")
#         if kwargs.get("student_name"):
#             error.student_name = kwargs.get("student_name")
#         error.save()
#         return cls(error=error)
