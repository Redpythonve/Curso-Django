from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


def herencias(request):
    return render(request, 'herencia.html', {})

def ejemploh(request):
    return render(request, 'ejemploh.html', {})

def otrah(request):
    return render(request, 'otrah.html', {})