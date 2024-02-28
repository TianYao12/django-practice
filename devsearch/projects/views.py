from django.shortcuts import render

from django.http import HttpResponse


def projects(request):
    return HttpResponse("here are oru proejc")


def project(request, pk):
    return HttpResponse('SINGLE PROJECT')
