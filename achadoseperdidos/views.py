from django.shortcuts import render, get_object_or_404, redirect
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
            return redirect('lista-de-itens')
    else:
        form = ObjetoForm()
    return render(request, 'adicionaritem.html', {'form': form})

def listadeitens(request):
    objetos = Objeto.objects.all()
    return render(request, 'listadeitens.html', {'objetos': objetos})

def item(request, id):
    objeto = get_object_or_404(Objeto, pk=id)
    return render(request, 'item.html', {'objeto': objeto})

def editar(request, id):
    objeto = get_object_or_404(Objeto, pk=id)
    form = ObjetoForm(instance=objeto)
    if(request.method == 'POST'):
        form = ObjetoForm(request.POST, instance=objeto)

        if(form.is_valid()):
            objeto.save()
            return redirect('/lista-de-itens')

        else:
            return render(request, 'editaritem.html', {'form': form, 'objeto': objeto})

    else:

        return render(request, 'editaritem.html', {'form': form, 'objeto': objeto})   


