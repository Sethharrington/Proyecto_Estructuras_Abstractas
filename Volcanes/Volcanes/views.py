'''
Created on Nov 1, 2021

@authors: Jesus Jimenez, Seth Harrington
'''

from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
def portada(request):

    #doc_externo = open("C:/Users/sbgha/OneDrive/Escritorio/Git_Hub/Proyecto_Estructuras_Abstractas/Volcanes/Volcanes/plantillas/plantilla1.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    
    doc_plantilla = loader.get_template('plantilla1.html')

    #ctx = Context()
    documento = doc_plantilla.render()
    return HttpResponse(documento)

def volcanes(request):
    doc_plantilla = loader.get_template('plantilla2.html')
    documento = doc_plantilla.render()
    return HttpResponse(documento)