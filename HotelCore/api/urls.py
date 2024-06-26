from django.urls import path, include

urlpatterns = [
    path('api/hotel', include('api.HotelAPI.urls')),
    path('api/', include('api.UserAPI.urls')),
]

