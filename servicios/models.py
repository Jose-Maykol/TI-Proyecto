from django.db import models

# Create your models here.
class Servicios(models.Model):

    tipo  = models.CharField(max_length = 20, verbose_name= "tipo de servicio")
    descripcion = models.CharField(max_length = 300, null = True, verbose_name= "Descripcion del servicio")
    precio = models.FloatField(null = True, verbose_name= "Precio")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Servicio"  