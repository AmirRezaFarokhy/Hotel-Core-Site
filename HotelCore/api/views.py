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
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


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
    lookup_field = 'pk'


class SignedUpAPIView(generics.CreateAPIView):
    serializer_class = UserProfilesSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = authenticate(request, username=request.data.get('username'), 
                            password=request.data.get('password'))
        if user is not None:
            login(request, user)
            request.session['username'] = request.data.get('username')
            request.session.save()
            return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/api/hotel')

    

class LogInAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]


class UserProfileAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]

