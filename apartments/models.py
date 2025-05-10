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

###

class ApartmentNew(models.Model):
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    currency = models.CharField(max_length=10)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    bathrooms = models.IntegerField()
    accommodates = models.IntegerField()
    public_summary = models.TextField()

    class Meta:
        db_table = 'apartments_apartmentnew'

    def __str__(self):
        return self.title
    
    @property
    def first_picture(self):
        first_pic = self.pictures.first()
        return first_pic.url if first_pic else None
    
    @property
    def base_price_int(self):
        return int(self.base_price)


class ApartmentPicture(models.Model):
    apartment = models.ForeignKey(ApartmentNew, on_delete=models.CASCADE, related_name='pictures')
    url = models.URLField()

    class Meta:
        db_table = 'apartments_pictures'

    def __str__(self):
        return f"Picture for {self.apartment.title}"


class Room(models.Model):
    apartment = models.ForeignKey(ApartmentNew, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.IntegerField()

    class Meta:
        db_table = 'apartments_rooms'

    def __str__(self):
        return f"Room {self.room_number} of {self.apartment.title}"


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'apartments_beds'

    def __str__(self):
        return f"{self.quantity} x {self.type} in Room {self.room.room_number}"


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'apartments_amenities'

    def __str__(self):
        return self.name


class ApartmentAmenity(models.Model):
    apartment = models.ForeignKey(ApartmentNew, on_delete=models.CASCADE, related_name='apartment_amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    class Meta:
        db_table = 'apartments_apartment_amenities'
        unique_together = ('apartment', 'amenity')

    def __str__(self):
        return f"{self.amenity.name} for {self.apartment.title}"
    
class ApartmentCountry(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'apartments_countries'

    def __str__(self):
        return self.name

class ApartmentCity(models.Model):
    country = models.ForeignKey(ApartmentCountry, on_delete=models.CASCADE, related_name='apartment_countries')
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'apartments_cities'

    def __str__(self):
        return self.name
    
class ApartmentNeighborhood(models.Model):
    city = models.ForeignKey(ApartmentCity, on_delete=models.CASCADE, related_name='apartment_neighborhoods')
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'apartments_neighborhoods'

    def __str__(self):
        return self.name