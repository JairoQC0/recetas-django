from django.shortcuts import render

from django.shortcuts import render
from .models import Receta

def lista_recetas(request):
    recetas = Receta.objects.all().order_by('-creado')
    return render(request, 'core/lista_recetas.html', {'recetas': recetas})