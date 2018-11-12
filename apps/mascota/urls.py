from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo', views.mascota_view, name='mascota_crear'),
    path('listar', views.mascota_list, name='mascota listar'),
    path('editar/<int:id_mascota>/', views.mascota_edit, name='mascota_editar')

]