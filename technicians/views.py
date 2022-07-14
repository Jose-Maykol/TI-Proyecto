from django.shortcuts import render
from technicians.form import TecnicoForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from technicians.models import Tecnico

class TecnicoCreateView(CreateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = "create_technician.html"
    success_url = '/technicians/list/'

class TecnicoListView(ListView):
    model = Tecnico
    template_name = "list_technicians.html"
