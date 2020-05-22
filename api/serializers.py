from rest_framework import serializers
from main.models import Profile
from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = ['firstname', 'lastname', 'email', 'phone', 'is_active', 'date_registered']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Token
        fields = ['user', 'key', 'created']