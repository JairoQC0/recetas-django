from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('crear/', views.crear_receta, name='crear_receta'),

]
