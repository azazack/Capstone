from django.contrib.auth import logout, authenticate, login
from rest_framework.views import APIView
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..models import User
import jwt, datetime
from ..modules import authenticated_user


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
            print('not logged')
            login(request, auth)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            'jwt': token
        })


class UserView(APIView):
    def get(self, request):
        return Response(authenticated_user(request))


class Logout(APIView):
    def delete(self, request):
        logout(request)
        return Response({
            'message': "logout"
        })


class UsersList(APIView):
    def get(self, request):
        name = request.GET.get('name')
        if not name:
            users = User.objects.all()
        else:
            users = User.objects.filter(name__contains=name)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
