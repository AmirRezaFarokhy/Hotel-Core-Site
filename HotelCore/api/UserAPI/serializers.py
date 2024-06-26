from HotelService.models import Hotel, City, DetailHotel
from rest_framework import serializers
from base.mixin import BaseDateMixin
from UserProfile.models import UserProfiles
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSignUpSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = make_password(validated_data['password'], salt=None, hasher='default')
        user = User.objects.create(
            username=validated_data['username'],
            password=password,
            first_name=validated_data['first_name']
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}



class UserLogInSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('id', 'username', 'password', )
        extra_kwargs = {'password': {'write_only': True}}
