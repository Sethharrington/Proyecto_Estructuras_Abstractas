from os import name
from django.urls import path
from . import views

app_name = "Covid19"

urlpatterns = [
    path("Reportes_Dashboard/",views.CovidDashboard,name="reportes"),
    path("Alajuela/",views.Alajuela,name="alajuela"),
    path("Cartago/",views.Cartago,name="cartago"),
    path("Guanacaste/",views.Guanacaste,name="guanacaste"),
    path("Heredia/",views.Heredia,name="heredia"),
    path("Limon/",views.Limon,name="limon"),
    path("Puntarenas/",views.Puntarenas,name="puntarenas"),
    path("SanJose/",views.SanJoseReport,name="sanjose"),
    path("ReporteProyectoFinal",views.ReporteFinal,name='reportefinal')
]
