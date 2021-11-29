'''
Created on Nov 1, 2021

@authors: Jesus Jimenez, Seth Harrington
'''

from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
def portada(request):
    return render(request, "plantilla1.html")

def volcanes(request):
    return render(request, "plantilla2.html")

