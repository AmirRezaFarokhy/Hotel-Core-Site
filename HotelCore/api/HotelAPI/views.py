from rest_framework import generics
from rest_framework import status
from HotelService.models import Hotel, DetailHotel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.HotelAPI.serializers import HotelSerializer, DetailHotelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from UserProfile.models import UserProfiles
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework import status


class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel_name']
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DetailHotelAPIView(generics.RetrieveAPIView):
    serializer_class = DetailHotelSerializer
    queryset = DetailHotel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    lookup_field = 'pk'
