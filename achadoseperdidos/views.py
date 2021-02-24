from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST, request.FILES)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.save()
            return redirect('listadeintens')
    else:
        form = ObjetoForm()
    return render(request, 'index.html')


def adicionaritem(request):
    return render(request, 'adicionaritem.html')

def listadeitens(request):
    return render(request, 'listadeitens.html')

