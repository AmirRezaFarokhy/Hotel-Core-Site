from HotelService.models import Hotel, City
from rest_framework import serializers
from base.mixin import BaseDateMixin

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer, BaseDateMixin):

    location = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    deleted_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return self.convert_date(obj.created_at)
    
    def get_updated_at(self, obj):
        return self.convert_date(obj.updated_at)
    
    def get_deleted_at(self, obj):
        return self.convert_date(obj.deleted_at)

    def get_location(self, obj):
        return obj.location.address

    class Meta:
        model = Hotel
        fields = '__all__'




