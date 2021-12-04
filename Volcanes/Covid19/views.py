from django.shortcuts import render
from Covid19.analysis import Analysis
from Covid19.analysis import ruta
# Create your views here.
fecha = ['14/07/2021','20/07/2021'] #fecha para pruebas
def CovidDashboard(request):
    costaRica = Analysis(ruta)
    costaRica.fecha = fecha
    costaRica.provincia()
    datosCostaRica = [costaRica.x,costaRica.y]
    return render(request, "Covid19/reportes.html", {"datos":datosCostaRica})

def ReporteFinal(request):
    return render(request, "Covid19/reporteproyecto.html")

def Alajuela(request):
    alajuela = Analysis(ruta)
    alajuela.fecha = fecha
    alajuela.cantonesProvincia("Alajuela")
    datoalajuela = []
    for i in range(len(alajuela.cantones)):
        alajuela.canton(alajuela.cantones[i])
        datoalajuela.append(alajuela.y)
    return render(request, "Covid19/alajuela.html", {"datos":datoalajuela,"fechas":fecha,"cantones":alajuela.cantones})

def Cartago(request):
    cartago = Analysis(ruta)
    cartago.fecha = fecha
    cartago.cantonesProvincia("Cartago")
    datocartago = []
    for i in range(len(cartago.cantones)):
        cartago.canton(cartago.cantones[i])
        datocartago.append(cartago.y)
    return render(request, "Covid19/cartago.html", {"datos":datocartago,"fechas":fecha,"cantones":cartago.cantones})

def Guanacaste(request):
    guanacaste = Analysis(ruta)
    guanacaste.fecha = fecha
    guanacaste.cantonesProvincia("Guanacaste")
    datoguanacaste = []
    for i in range(len(guanacaste.cantones)):
        guanacaste.canton(guanacaste.cantones[i])
        datoguanacaste.append(guanacaste.y)
    return render(request, "Covid19/guanacaste.html", {"datos":datoguanacaste,"fechas":fecha,"cantones":guanacaste.cantones})

def Heredia(request):
    heredia = Analysis(ruta)
    heredia.fecha = fecha
    heredia.cantonesProvincia("Heredia")
    datoheredia = []
    for i in range(len(heredia.cantones)):
        heredia.canton(heredia.cantones[i])
        datoheredia.append(heredia.y)
    return render(request, "Covid19/heredia.html", {"datos":datoheredia,"fechas":fecha,"cantones":heredia.cantones})

def Limon(request):
    limon = Analysis(ruta)
    limon.fecha = fecha
    limon.cantonesProvincia("Limon")
    datolimon = []
    for i in range(len(limon.cantones)):
        limon.canton(limon.cantones[i])
        datolimon.append(limon.y)
    return render(request, "Covid19/limon.html", {"datos":datolimon,"fechas":fecha,"cantones":limon.cantones})

def Puntarenas(request):
    puntarenas = Analysis(ruta)
    puntarenas.fecha = fecha
    puntarenas.cantonesProvincia("Puntarenas")
    datopuntarenas = []
    for i in range(len(puntarenas.cantones)):
        puntarenas.canton(puntarenas.cantones[i])
        datopuntarenas.append(puntarenas.y)
    return render(request, "Covid19/puntarenas.html", {"datos":datopuntarenas,"fechas":fecha,"cantones":puntarenas.cantones})

def SanJoseReport(request):
    sanJose = Analysis(ruta)
    sanJose.fecha = fecha
    sanJose.cantonesProvincia("San Jose")
    datosanJose = []
    for i in range(len(sanJose.cantones)):
        sanJose.canton(sanJose.cantones[i])
        datosanJose.append(sanJose.y)
    
    return render(request, "Covid19/sanjose.html", {"datos":datosanJose,"fechas":fecha,"cantones":sanJose.cantones})
