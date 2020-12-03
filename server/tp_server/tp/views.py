from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from .models import Error, Problem
ENABLED = False


def test_view(View):
    if ENABLED:
        queryset = Error.objects.filter(problem__problem_number='21_1')
        # queryset = Problem.objects.all()
        return HttpResponse([vars(item) for item in queryset])
    else:
        return HttpResponse("No Test Views Are Enabled")

@method_decorator(csrf_exempt, name='dispatch')
class PrivateGraphQLView(GraphQLView):
    pass

@method_decorator(csrf_exempt, name='dispatch')
class CompanionAppGraphQLView(GraphQLView):
    pass
