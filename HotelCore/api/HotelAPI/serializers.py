from HotelService.models import Hotel, City, DetailHotel
from rest_framework import serializers
from base.mixin import BaseDateMixin

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer, BaseDateMixin):

    detail_url = serializers.HyperlinkedIdentityField(view_name='hotel-detail')

    class Meta:
        model = Hotel
        fields = ("id", "hotel_name", "price", "image", 'detail_url')



class DetailHotelSerializer(serializers.ModelSerializer, BaseDateMixin):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    deleted_at = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    hotel = serializers.SerializerMethodField()
    stars = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_stars(self, obj):
        return obj.hotel.stars

    def get_phone(self, obj):
        return obj.hotel.phone

    def get_price(self, obj):
        return obj.hotel.price

    def get_created_at(self, obj):
        return self.convert_date(obj.created_at)
    
    def get_updated_at(self, obj):
        return self.convert_date(obj.updated_at)
    
    def get_deleted_at(self, obj):
        return self.convert_date(obj.deleted_at)
    
    def get_address(self, obj):
        return obj.hotel.location.address

    def get_hotel(self, obj):
        return obj.hotel.hotel_name
    
    

    class Meta:
        model = DetailHotel
        fields = ('id', 'hotel', 'address', 
                  'stars', 'phone', 'price',
                  'image_one', 'image_two',
                  'image_three', "image_four",
                  'updated_at', 'created_at', 
                  'deleted_at')
