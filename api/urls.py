from django.urls import path, include
from .views import ProfileApi

urlpatterns = [
    path('profiles/', ProfileApi.as_view(), name = 'profiles'),
]