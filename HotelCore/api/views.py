from rest_framework import generics
from rest_framework import status
from HotelService.models import Hotel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializers import HotelSerializer

class HotelListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


