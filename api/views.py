from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Profile
from api.serializers import ProfileSerializer, TokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

##Authentication for function based api views
from rest_framework.decorators import authentication_classes, permission_classes

###Authentication and permissions for class blassed views###
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
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

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def token_view(request):

    if request.method == 'GET':
        tokens = Token.objects.all()
        serializer = TokenSerializer(tokens, many =True)

        return Response(serializer.data)
    # return render(request, 'token.html', {'tokens' : tokens})