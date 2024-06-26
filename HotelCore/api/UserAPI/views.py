from rest_framework import generics
from rest_framework import status
from HotelService.models import Hotel, DetailHotel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.UserAPI.serializers import UserProfilesSerializer
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


class DeleteAccountAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = UserProfilesSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        logout(request)
        Session.objects.filter(session_key=request.session.session_key).delete()
        print(request.session['username'])
        User.objects.filter(username=request.session['username']).delete()
        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/api/hotel')
    
    def get(self, request, *args, **kwargs):
        userprofile = request.session['username']
        response = {
            "user": userprofile
        }
        return Response(response, status=status.HTTP_202_ACCEPTED)


class LogOutAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfilesSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/api/hotel')


class UserProfileAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]