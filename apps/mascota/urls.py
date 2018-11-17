from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo', views.MascotaCreate.as_view(), name='mascota_crear'),
    path('listar', views.MascotaList.as_view(), name='mascota listar'),
    path('editar/<pk>/', views.MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<pk>/', views.MascotaDelete.as_view(), name='mascota_eliminar'),
]