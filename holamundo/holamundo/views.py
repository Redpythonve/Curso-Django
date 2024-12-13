from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Buenos días")

def despedida(request):
    return HttpResponse("Adiós desde Django")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse(" Eres Adulto puedes Entrar")
    else:
        return HttpResponse(" Eres Menor de Edad")