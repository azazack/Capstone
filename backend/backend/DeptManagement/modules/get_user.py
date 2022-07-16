from rest_framework.exceptions import AuthenticationFailed
import jwt
from ..models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


def authenticated_user(request):
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
        return serializer.data
    else:
        return Response({
            'message': "You are not logged in"
        }, status=status.HTTP_401_UNAUTHORIZED)
