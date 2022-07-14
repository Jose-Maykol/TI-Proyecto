from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.TecnicoCreateView.as_view(), name= 'create_technician'),
    path('list/', views.TecnicoListView.as_view(), name='list_technicians'),
]