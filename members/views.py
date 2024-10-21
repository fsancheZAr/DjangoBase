from django.shortcuts import render
from django.http import HttpResponse


def members(request): #nombre de la vista "members"
    return HttpResponse('Hello world!')
