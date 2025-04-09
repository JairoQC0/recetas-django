from django.shortcuts import render, redirect, get_object_or_404
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

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'core/detalle_receta.html', {'receta': receta})

def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('detalle_receta', receta_id=receta.id)
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'core/editar_receta.html', {'form': form, 'receta': receta})

def eliminar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'core/eliminar_receta.html', {'receta': receta})

