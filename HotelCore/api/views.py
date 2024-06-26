from rest_framework import generics
from rest_framework import status
from HotelService.models import Hotel, DetailHotel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializers import (
    HotelSerializer, 
    DetailHotelSerializer,
    UserProfilesSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from UserProfile.models import UserProfiles
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User 
from rest_framework.authentication import SessionAuthentication, BaseAuthentication


class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel_name']


class DetailHotelAPIView(generics.RetrieveAPIView):
    serializer_class = DetailHotelSerializer
    queryset = DetailHotel.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


class SignedUpAPIView(generics.CreateAPIView):
    serializer_class = UserProfilesSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()


class LogInAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]


class UserProfileAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]

