from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from .models import Error, Problem
ENABLED = True

def test_view(View):
    if ENABLED:
        queryset = Error.objects.filter(problem__problem_number='21_1')
        # queryset = Problem.objects.all()
        return HttpResponse([vars(item) for item in queryset])
    else:
        return HttpResponse("No Test Views Are Enabled")
