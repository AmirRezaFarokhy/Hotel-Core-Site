from django.db import models
from base.models import BaseModel


class State(models.Model):
    state = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.state


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField()

    def __str__(self) -> str:
        return f"{self.state} -- {self.city}"


class Hotel(BaseModel):

    class PutStart(models.IntegerChoices):
        VERYGOOD = 5
        GOOD = 4
        NOTBADNOTGOOD = 3
        BAD = 2
        VERYBAD = 1


    hotel_name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='Hotel/')
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    stars = models.IntegerField(default=3, choices=PutStart.choices)
    price = models.IntegerField()
    phone = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.hotel_name} -- {self.stars} -- {self.id}"


class DetailHotel(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel')
    image_one = models.ImageField(blank=True, null=True, upload_to='details/')
    image_two = models.ImageField(blank=True, null=True, upload_to='details/')
    image_three = models.ImageField(blank=True, null=True, upload_to='details/')
    image_four = models.ImageField(blank=True, null=True, upload_to='details/')
    
    def __str__(self):
        return f"{self.hotel.hotel_name} -- {self.hotel.stars} -- detail"


