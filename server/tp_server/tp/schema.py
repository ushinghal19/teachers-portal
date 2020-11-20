import graphene
from graphene_django_extras import DjangoFilterListField, DjangoObjectField
from .object_types import ErrorType, ProblemType, AssignmentType, TeacherType
from .mutations import ErrorMutationCreate, ProblemMutationCreate, AssignmentMutationCreate, \
    TeacherMutationCreate


class Query(graphene.ObjectType):
    # These root queries return a single object, and require an ID param.
    hypatia_error = DjangoObjectField(ErrorType)

    problem = DjangoObjectField(ProblemType)

    assignment = DjangoObjectField(AssignmentType)

    teacher = DjangoObjectField(TeacherType)

    # These root queries return a list of objects, and can be filtered.
    hypatia_errors = DjangoFilterListField(ErrorType)

    problems = DjangoFilterListField(ProblemType)

    assignments = DjangoFilterListField(AssignmentType)

    teachers = DjangoFilterListField(TeacherType)

    # If you needed to do a custom resolver, you would do it this way.
    # But, the django_graphene_extras package is doing this for us above.
    # @staticmethod
    # def resolve_hypatia_error(root, info, **kwargs):
    #     return Error.objects.all()


class Mutation(graphene.ObjectType):
    """
    Defines all Mutations for this Query
    """
    create_new_error = ErrorMutationCreate.Field()
    # THE BELOW TWO MUTATIONS HAVE NOT BEEN UPDATED FOR NEW MODELS
    # create_new_error_with_id = HypatiaErrorMutationWithID.Field()
    # update_error = HypatiaErrorUpdate.Field()
    create_new_problem = ProblemMutationCreate.Field()
    create_new_assignment = AssignmentMutationCreate.Field()
    create_new_teacher = TeacherMutationCreate.Field()


# ======================== REGISTER QUERY & MUTATION CLASSES =======================================

schema = graphene.Schema(query=Query, mutation=Mutation)
