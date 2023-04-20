from django.db import models
from django.contrib.auth.models import User

class Propiedades(models.Model):
    Propiedad_Descripcion = models.CharField(max_length=200)
    Propiedad_Direccion =  models.CharField(max_length=200)
    Numero_Habitaciones = models.PositiveIntegerField()
    Propiedad_Costo = models.PositiveIntegerField()
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="propiedades", null=True, blank=True)
    Fecha_Publicacion = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.id} -- {self.Propiedad_Descripcion} -- {self.Fecha_Publicacion}"

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    Email = models.EmailField(blank=True)
    Web = models.URLField(null=True,blank=True)
    imagen = models.ImageField(upload_to="profiles", null=True, blank=True)