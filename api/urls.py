from django.urls import path, include
from .views import ProfileApi, token_view

urlpatterns = [
    path('profiles/', ProfileApi.as_view(), name = 'profiles'),
    path('tokens/', token_view, name='token')
]