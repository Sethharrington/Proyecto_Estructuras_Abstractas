from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def CovidDashboard(request):
    plantilla = "Covid19/reportes.html"
    return render(request, plantilla)

def SanJoseReport(request):
    plantilla1 = "Covid19/sanjose.html"
    return render(request, plantilla1)