from django.shortcuts import render
from .models import Objeto
from .forms import ObjetoForm

def home(request):
    
    return render(request, 'index.html')


def adicionaritem(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST, request.FILES)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.save()
            return redirect('listadeintens')
    else:
        form = ObjetoForm()
    return render(request, 'adicionaritem.html', {'form': form})

def listadeitens(request):
    return render(request, 'listadeitens.html')

