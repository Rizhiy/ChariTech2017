from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def profile(request, pk):
    return HttpResponse("Profile {}".format(pk))
