from django.urls import path
from api.views import HotelListAPIView

urlpatterns = [
    path('api/hotel', HotelListAPIView.as_view(), name='hotel-list')
]

