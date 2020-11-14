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
            error.error_type = kwargs.get("student_name")
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
    create_new_error = HypatiaErrorMutationCreate.Field()
    create_new_error_with_id = HypatiaErrorMutationWithID.Field()
    update_error = HypatiaErrorUpdate.Field()


# ======================== REGISTER QUERY & MUTATION CLASSES =======================================

schema = graphene.Schema(query=Query, mutation=Mutation)



