from django.urls import path
from api.views import HotelListAPIView, DetailHotelAPIView

urlpatterns = [
    path('api/hotel', HotelListAPIView.as_view(), name='hotel-list'),
    path('api/hotel/detail/<int:pk>', DetailHotelAPIView.as_view(), name='hotel-detail'),
]

