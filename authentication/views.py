from datetime import datetime, timezone, timedelta
from django.utils import timezone
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myproject.settings import SECRET_KEY
from .serializers import UserSerializer, LoginSerializer
from .models import User


class Registation(APIView):


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        if not email and not password:
            return Response({'error': 'Either email or password is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            token = self.genarate_token(user)
            return Response({'token': token}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def genarate_token(self, user):
        exptime = timezone.now() + timedelta(minutes=30)

        payload = {
            'user_id': user.id,
            'name': user.username,
            'exp': exptime,

        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

class Users(APIView):
    authentication_classes = []
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class AllUsers(APIView):
    authentication_classes = []
    def get(self, request):
        number_of_user = User.objects.count()
        return Response({'number_of_user': number_of_user})






