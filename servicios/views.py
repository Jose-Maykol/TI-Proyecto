from django.shortcuts import render,get_object_or_404
from .models import Servicios

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
    return render(request,'it_service_detail.html',context)