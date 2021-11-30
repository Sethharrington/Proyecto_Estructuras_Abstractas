from django.shortcuts import render
from django.http import JsonResponse
from Covid19.analysis import Analysis
# Create your views here.
'''fecha = ['14/07/2021','20/07/2021'] #fecha para pruebas
obj = Analysis('./07_20_21_CSV_ACTIVOS_UTF8.csv')

obj.x
obj.y
obj.canton('Sarapiquí', fecha )
#obj.canton('San Carlos', fecha )
obj.Acotar(fecha,['Acosta','Alajuelita'])'''
def CovidDashboard(request):
    plantilla = "Covid19/reportes.html"
    return render(request, plantilla)

def SanJoseReport(request):
    datosx = [125, 100, 3, 25, 2, 3]
    plantilla1 = "Covid19/sanjose.html"
    return render(request, plantilla1, {"datosx":datosx})