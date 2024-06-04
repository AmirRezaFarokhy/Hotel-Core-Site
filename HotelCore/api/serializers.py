from HotelService.models import Hotel, City
from rest_framework import serializers
 

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):

    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        return obj.location.address

    class Meta:
        model = Hotel
        fields = '__all__'




