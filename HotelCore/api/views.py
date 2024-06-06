from rest_framework import generics
from rest_framework import status
from HotelService.models import Hotel, DetailHotel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializers import HotelSerializer, DetailHotelSerializer

class HotelListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class DetailHotelAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DetailHotelSerializer
    queryset = DetailHotel.objects.all()
    lookup_field = 'pk'


