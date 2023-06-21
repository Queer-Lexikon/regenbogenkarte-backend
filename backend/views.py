from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from .models import Organisation
from django.forms.models import model_to_dict

import json

def orgs_json(request):
    response = JsonResponse([org.to_dict() for org in Organisation.objects.iterator()], safe=False)

    return response

# Create your views here.
