from django.urls import path
from api.UserAPI.views import (
    SignedUpAPIView,
    LogInAPIView,
    UserProfileAPIView,
    LogOutAPIView,
)

urlpatterns = [
    path('signup/', SignedUpAPIView.as_view(), name='signup-view'),
    path('logout/', LogOutAPIView.as_view(), name='logout-view'),
    path('login/', LogInAPIView.as_view(), name='login-view'),
]

