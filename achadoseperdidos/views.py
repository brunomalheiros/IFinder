from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def adicionaritem(request):
    return render(request, 'adicionaritem.html')

def listadeitens(request):
    return render(request, 'listadeitens.html')

