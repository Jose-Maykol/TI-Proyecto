from django.contrib import admin
from django.urls import path
from servicios.views import(
    listServicios,
    DetallesServicio,
    )

urlpatterns = [
    path('listar/', listServicios, name= 'lista_Servicios'),
    path('<int:myID>/', DetallesServicio, name = 'Detalles_Servicio'),
    path('agregar/', generarServicio, name = 'Creacion_Servicio'),
]
