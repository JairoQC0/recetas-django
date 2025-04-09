from django.shortcuts import render, redirect
from .forms import RecetaForm
from .models import Receta

def lista_recetas(request):
    recetas = Receta.objects.all().order_by('-creado')
    return render(request, 'core/lista_recetas.html', {'recetas': recetas})

def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'core/crear_receta.html', {'form': form})