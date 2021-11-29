from django.urls import path
from . import views

app_name = "Covid19"

urlpatterns = [
    path("Reportes_Dashboard/",views.CovidDashboard,name="reportes"),
    path("SanJose/",views.SanJoseReport,name="sanjose"),
]
