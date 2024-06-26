from django.db import models
from HotelService.models import Hotel
from django.contrib.auth.models import User 


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username



