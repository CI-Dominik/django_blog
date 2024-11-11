from django.shortcuts import render # noqa
from django.http import HttpResponse


def blog(request):
    return HttpResponse("Hello, Blog!")
