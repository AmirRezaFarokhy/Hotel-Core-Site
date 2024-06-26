from django.urls import path
from api.views import (
    HotelListAPIView, 
    DetailHotelAPIView,
    SignedUpAPIView,
    LogInAPIView,
    UserProfileAPIView,
    LogOutAPIView,
)

urlpatterns = [
    path('api/hotel', HotelListAPIView.as_view(), name='hotel-list'),
    path('api/hotel/detail/<int:pk>', DetailHotelAPIView.as_view(), name='hotel-detail'),
    path('api/signup/', SignedUpAPIView.as_view(), name='signup-view'),
    path('api/logout/', LogOutAPIView.as_view(), name='logout-view'),
]

