from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Profile
from api.serializers import ProfileSerializer

###Authentication and permissions for class blassed views###
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProfileApi(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Profile.objects.all()
        serializer = ProfileSerializer(articles, many =True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

