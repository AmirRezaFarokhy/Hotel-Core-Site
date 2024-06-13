from rest_framework import generics
from rest_framework import status
from HotelService.models import Hotel, DetailHotel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializers import HotelSerializer, DetailHotelSerializer
from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import filters
from rest_framework import filters

class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel_name']


class DetailHotelAPIView(generics.RetrieveAPIView):
    serializer_class = DetailHotelSerializer
    queryset = DetailHotel.objects.all()
    lookup_field = 'pk'


