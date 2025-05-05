from django.db import models
from django.contrib.auth.models import User
from apartments.models import Apartment

class Reservation(models.Model):
    Apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f"Reservacion hecha por {self.user.username} desde {self.start_date} hasta {self.end_date}"
