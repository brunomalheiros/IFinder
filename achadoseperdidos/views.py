from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Objeto
from .forms import ObjetoForm
from django.contrib.auth.models import User
from accounts.forms import UserForm, PerfilForm
from django.contrib.auth.models import User
from accounts.models import Perfil

def home(request):
    
    return render(request, 'index.html')

@login_required
def adicionaritem(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST, request.FILES)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.user = request.user
            objeto.save()
            return redirect('lista-de-itens')
    else:
        form = ObjetoForm()
    return render(request, 'adicionaritem.html', {'form': form})


@login_required
def listadeitens(request):
    objetos = Objeto.objects.all()
    return render(request, 'listadeitens.html', {'objetos': objetos})

@login_required
def myposts(request):
    objetos = Objeto.objects.all().filter(user=request.user)
    return render(request, 'myposts.html', {'objetos': objetos})


@login_required
def item(request, id):
    objeto = get_object_or_404(Objeto, pk=id)
    return render(request, 'item.html', {'objeto': objeto})


@login_required
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




