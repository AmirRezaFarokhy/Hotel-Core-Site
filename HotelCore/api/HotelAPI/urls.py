from django.urls import path
from api.HotelAPI.views import (
    HotelListAPIView, 
    DetailHotelAPIView,
)

urlpatterns = [
    path('', HotelListAPIView.as_view(), name='hotel-list'),
    path('detail/<int:pk>', DetailHotelAPIView.as_view(), name='hotel-detail'),
]

