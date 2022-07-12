from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime
from rest_framework import status


# Create your views here.

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data['user'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        user = request.data['user']
        email = user['email']
        password = user['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Wrong Credentials')

        auth = authenticate(request, email=email, password=password)
        if auth is not None:
            login(request, auth)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            'jwt': token
        })

class UserView(APIView):
    def get(self, request):
        if 'authorization' in request.headers:
            token = request.headers['authorization']

            if not token:
                raise AuthenticationFailed("Unauthenticated")

            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed("Unauthenticated")

            user = User.objects.get(id=payload['id'])
            serializer = UserSerializer(user)
            print(user.is_authenticated)
            return Response(serializer.data)
        else:
            return Response({
                'message': "You are not logged in"
            }, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def delete(self, request):
        logout(request)
        return Response({
            'message': "logout"
        })
