import graphene
from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoFilterListField, DjangoObjectField
from .models import Error, Problem, Assignment, Teacher
from .statistics import aggregate_errors, problem_errors, students_by_errors, type_of_errors

s = "goodbye"

# ======================== DEFINING THE OBJECT TYPES & MUTATIONS====================================
class StatisticType(DjangoObjectType):
    """
    Object type for statistics that we are gathering
    """

    aggregate_errors = graphene.Int()
    problem_errors = graphene.Int()
    type_of_errors = graphene.JSONString()
    students_by_errors = graphene.JSONString()

    def resolve_aggregate_errors(parent, info):
        return aggregate_errors(parent)

    def resolve_problem_errors(parent, info):
        return problem_errors(parent)

    def resolve_type_of_errors(parent, info):
        return type_of_errors(parent)

    def resolve_students_by_errors(parent, info):
        return students_by_errors(parent)


class ProblemType(DjangoObjectType):
    """
    Object type for each problem in an assignment.
    """

    class Meta:
        model = Problem
        fields = ('problem_id', )
        filter_fields = ['problem_id']

    statistic = graphene.Field(StatisticType)

class AssignmentType(DjangoObjectType):
    """
    Object type for each Assignment
    """
    class Meta:
        model = Assignment
        fields = ('assignment_id', )
        filter_fields = ['assigmnent_id']

    statistic = graphene.Field(StatisticType)

class HypatiaErrorType(DjangoObjectType):
    """
    Object Type for Errors from Hypatia.
    """
    class Meta:
        model = Error
        fields = ('error_id', 'error_type', 'student_name')
        filter_fields = ['error_id', 'error_type', 'student_name']


class HypatiaErrorMutationCreate(graphene.Mutation):
    """
    Mutation for Errors from Hypatia.
    """
    class Arguments:
        error_type = graphene.String()
        student_name = graphene.String()

    error = graphene.Field(HypatiaErrorType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        """
        Takes optional additional Error fields and creates a new error.
        """
        error = Error(kwargs)
        error.save()
        return cls(error=error)


class HypatiaErrorMutationWithID(graphene.Mutation):
    """
    Mutation for Errors from Hypatia, when you specify an ID (from the Hypatia Companion App).
    """
    class Arguments:
        id = graphene.String()
        error_type = graphene.String()
        student_name = graphene.String()

    error = graphene.Field(HypatiaErrorType)

    @classmethod
    def mutate(cls, root, info, id: str, **kwargs):
        """
        Requires an ID method. Takes optional additional Error fields, and either updates
        or creates the required field.
        """
        error, created = Error.objects.update_or_create(pk=id,
                                                        defaults=kwargs)
        return cls(error=error)


class HypatiaErrorUpdate(HypatiaErrorMutationWithID):
    """
    Updates specified fields for Hypatia Errors from Hypatia, when you specify an ID.
    """

    @classmethod
    def mutate(cls, root, info, id: str, **kwargs):
        """
        Requires an ID method. Takes optional additional Error fields and performs update.
        """
        error = Error.objects.get(pk=id)
        if kwargs.get("error_type"):
            error.error_type = kwargs.get("error_type")
        if kwargs.get("student_name"):
            error.student_name = kwargs.get("student_name")
        error.save()
        return cls(error=error)


# ======================== DEFINING THE QUERY & MUTATION OBJECTS ===================================


class Query(graphene.ObjectType):
    # These are demo top-level fields that should be deleted before publishing.
    hello = graphene.String(default_value="Hi!")
    new_field = graphene.String(default_value=s)

    # This root query returns a single object, and requires an ID param.
    hypatia_error = DjangoObjectField(HypatiaErrorType)

    # This root query returns a list of objects, and can be filtered.
    hypatia_errors = DjangoFilterListField(HypatiaErrorType)

    assignment = DjangoObjectField(AssignmentType)

    assignments = DjangoFilterListField(AssignmentType)

    problem = DjangoObjectField(ProblemType)

    problems = DjangoFilterListField(ProblemType)

    # If you needed to do a custom resolver, you would do it this way.
    # But, the django_graphene_extras package is doing this for us above.
    # @staticmethod
    # def resolve_hypatia_error(root, info, **kwargs):
    #     return Error.objects.all()


class Mutation(graphene.ObjectType):
    """
    Defines all Mutations for this Query
    """
    create_new_error = HypatiaErrorMutationCreate.Field()
    create_new_error_with_id = HypatiaErrorMutationWithID.Field()
    update_error = HypatiaErrorUpdate.Field()


# ======================== REGISTER QUERY & MUTATION CLASSES =======================================

schema = graphene.Schema(query=Query, mutation=Mutation)



