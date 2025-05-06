from django.db import models

# Create your models here.

class Apartment(models.Model):
    Name = models.CharField(max_length=200)
    Barrio = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)
    N_Personas = models.IntegerField(default=1)
    N_Banos =  models.IntegerField(default=1)
    N_Camas = models.IntegerField(default=1)
    ImagePath = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Name
    