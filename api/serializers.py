from rest_framework import serializers
from main.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = ['firstname', 'lastname', 'email', 'phone', 'is_active', 'date_registered']