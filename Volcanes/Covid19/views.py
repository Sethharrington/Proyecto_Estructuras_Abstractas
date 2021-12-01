from django.shortcuts import render
from django.http import JsonResponse
from Covid19.analysis import Analysis
# Create your views here.
fecha = ['14/07/2021','20/07/2021'] #fecha para pruebas
obj = Analysis('Covid19/archivosDeDatos/07_20_21_CSV_ACTIVOS_UTF8.csv')
obj.x
obj.y
obj.canton('Acosta',fecha)
casos_Nuevos = []
fechas = []
for i in obj.y:
    casos_Nuevos.append(i)
obj.Acotar(fecha,['Acosta','Alajuelita'])
def CovidDashboard(request):
    plantilla = "Covid19/reportes.html"
    return render(request, plantilla)

def SanJoseReport(request):
    obj = Analysis('Covid19/archivosDeDatos/07_20_21_CSV_ACTIVOS_UTF8.csv')
    datosAcosta = []
    datosAlajuelita= []
    sanJose = [datosAcosta, datosAlajuelita]
    fechas = []
    for i in obj.x:
        fechas.append(i)
    obj.canton(['Acosta','Alajuelita'],fecha)
    for i in obj.y.loc['Acosta',:]:
        datosAcosta.append(i)
    for i in obj.y.loc['Alajuelita',:]:
        datosAlajuelita.append(i)
    plantilla1 = "Covid19/sanjose.html"
    return render(request, plantilla1, {"datos":sanJose,"fechas":fechas})