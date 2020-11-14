import graphene
from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoFilterListField, DjangoObjectField
from .models import Error, Problem, Assignment, Teacher

s = "goodbye"

# ======================== DEFINING THE OBJECT TYPES & MUTATIONS====================================


class HypatiaErrorType(DjangoObjectType):
    """
    Object Type for Errors from Hypatia.
    """
    class Meta:
        model = Error
        fields = ('id', 'error_type', 'student_name')
        filter_fields = ['id', 'error_type', 'student_name']


class HypatiaErrorMutation(graphene.Mutation):
    """
    Mutation for Errors from Hypatia.
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


# ======================== DEFINING THE QUERY & MUTATION OBJECTS ===================================


class Query(graphene.ObjectType):
    # These are demo top-level fields that should be deleted before publishing.
    hello = graphene.String(default_value="Hi!")
    new_field = graphene.String(default_value=s)

    # This root query returns a single object, and requires an ID param.
    hypatia_error = DjangoObjectField(HypatiaErrorType)

    # This root query returns a list of objects, and can be filtered.
    hypatia_errors = DjangoFilterListField(HypatiaErrorType)

    # If you needed to do a custom resolver, you would do it this way.
    # But, the django_graphene_extras package is doing this for us above.
    # @staticmethod
    # def resolve_hypatia_error(root, info, **kwargs):
    #     return Error.objects.all()


class Mutation(graphene.ObjectType):
    """
    Defines all Mutations for this Queryt
    """
    create_new_error = HypatiaErrorMutation.Field()


# ======================== REGISTER QUERY & MUTATION CLASSES =======================================

schema = graphene.Schema(query=Query, mutation=Mutation)



