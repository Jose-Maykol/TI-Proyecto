from django.shortcuts import render,get_object_or_404
from .models import Servicios
frim .forms import ServiceForm
# Create your views here.
def listServicios(request):
    context = {
        'servicios' : Servicios.objects.all(),
        }
    return render(request, "it_service_list.html", context)

def DetallesServicio(request,myID):
    obj = get_object_or_404(Servicios, id = myID)
    context = {
        'objecto':obj
   }
    return render(request,'it_service_detail.html', context)

def generarServicio(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
      form.save()
      form = ServiceForm()
        
    context = {
        'form' = form
    }
    return render(request, 'formularioServicio.html', context)
