import graphene
from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoFilterListField, DjangoObjectField
from .models import Error, Problem, Assignment, Teacher
from .statistics import aggregate_errors, problem_errors, students_by_errors, type_of_errors

s = "goodbye"

# ======================== DEFINING THE OBJECT TYPES & MUTATIONS====================================


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
        error_id = graphene.String()
        error_type = graphene.String()
        student_name = graphene.String()
        problem_number = graphene.Int()
        assignment_id = graphene.String()

    error = graphene.Field(HypatiaErrorType)

    @classmethod
    def mutate(cls, root, info, error_id: str, error_type: str, student_name: str, problem_number: int,
               assignment_id: str):
        """
        Takes optional additional Error fields and creates a new error.
        """
        error = Error.create(error_id=error_id, error_type=error_type, student_name=student_name,
                             problem_number=problem_number, assignment_id=assignment_id)

        # error.save()
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


class StatisticType(graphene.ObjectType):
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
        fields = ('problem_number',)
        filter_fields = ['problem_number']

    errors = graphene.List(HypatiaErrorType)

    def resolve_errors(parent, info):
        return parent.errors


class ProblemMutationCreate(graphene.Mutation):
    """
    Mutation for problems from Hypatia.
    """
    class Arguments:
        problem_number = graphene.String()
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


class AssignmentType(DjangoObjectType):
    """
    Object type for each Assignment
    """
    class Meta:
        model = Assignment
        fields = ('assignment_id',)
        filter_fields = ['assignment_id']

    problems = graphene.List(ProblemType)
    statistic = graphene.Field(StatisticType)

    def resolve_problems(parent, info):
        return parent.problems

    def resolve_statistic(parent, info):
        return StatisticType(parent=parent)


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
        # assignment.save()
        return cls(assignment=assignment)


class TeacherType(DjangoObjectType):
    """
    Object type for each Assignment
    """
    class Meta:
        model = Teacher
        fields = ('teacher_id', 'teacher_name')
        filter_fields = ['teacher_id', 'teacher_name']

    assignments = graphene.List(AssignmentType)

    def resolve_problems(parent, info):
        return parent.assignments


# ======================== DEFINING THE QUERY & MUTATION OBJECTS ===================================


class Query(graphene.ObjectType):
    # These are demo top-level fields that should be deleted before publishing.
    hello = graphene.String(default_value="Hi!")
    new_field = graphene.String(default_value=s)

    # These root queries return a single object, and require an ID param.
    hypatia_error = DjangoObjectField(HypatiaErrorType)

    problem = DjangoObjectField(ProblemType)

    assignment = DjangoObjectField(AssignmentType)

    teacher = DjangoObjectField(TeacherType)

    # These root queries return a list of objects, and can be filtered.
    hypatia_errors = DjangoFilterListField(HypatiaErrorType)

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
    create_new_error = HypatiaErrorMutationCreate.Field()
    create_new_error_with_id = HypatiaErrorMutationWithID.Field()
    update_error = HypatiaErrorUpdate.Field()
    create_new_problem = ProblemMutationCreate.Field()
    create_new_assignment = AssignmentMutationCreate.Field()


# ======================== REGISTER QUERY & MUTATION CLASSES =======================================

schema = graphene.Schema(query=Query, mutation=Mutation)



