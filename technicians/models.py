from django.db import models

class Tecnico(models.Model):

    DNI = models.CharField(max_length= 8,verbose_name= "DNI")
    name = models.CharField(max_length= 50,verbose_name='Nombre del tecnico')
    address = models.CharField(max_length= 50,verbose_name='Direccion')
    city = models.CharField(max_length= 50,verbose_name= 'Ciudad')
    phone_number = models.CharField(max_length= 9,verbose_name= 'Numero de telefono')
    email = models.EmailField(verbose_name='Email')
    service_hours = models.CharField(max_length=50, verbose_name= 'Horario de servicio')

    class Meta:

        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnico'

    def __str__(self):
        return self.name
