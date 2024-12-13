from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html', {})

def dinámico(request, name):
    categorias = ['code', 'design', 'marketing', 'devweb', 'mba']
    context = {'name' : name, 'categorias' : categorias}
    return render(request, 'dinamico.html', context)
