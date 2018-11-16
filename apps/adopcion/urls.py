from django.urls import path
from . import views

urlpatterns = [


    path('solicitud/listar',views.SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', views.SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<pk>/', views.SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solictud/eliminar/<pk>/', views.SolicitudDelete.as_view(), name= 'solicitud_delete')
]