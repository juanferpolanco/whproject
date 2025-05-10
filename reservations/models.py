from django.db import models
from django.contrib.auth.models import User
from apartments.models import Apartment, ApartmentNew

class Reservation(models.Model):
    Apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='Reservation')
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f"Reservacion hecha por {self.user.username} desde {self.start_date} hasta {self.end_date}"

class ReservationNew(models.Model):
    apartment = models.ForeignKey(
        ApartmentNew,
        on_delete=models.CASCADE,
        related_name='reservations_new'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_reservations_new'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"ReservationNew for {self.apartment.title} by {self.user.username} from {self.start_date} to {self.end_date}"

