
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth.models import User
import jwt
import datetime
from rest_framework.authentication import get_authorization_header

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = 'HS256'
TOKEN_EXPIRATION_MINUTES = 60

def generate_jwt(user):
    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': exp,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, exp

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload, True, 'Token is valid'
    except jwt.ExpiredSignatureError:
        return None, False, 'Token has expired'
    except jwt.InvalidTokenError:
        return None, False, 'Invalid token'

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, exp = generate_jwt(user)
            return Response({
                'token': token,
                'expires': exp.replace(microsecond=0).isoformat() + 'Z'
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class VerifyTokenView(APIView):
    def post(self, request):
        token = request.data.get('token')
        payload, valid, message = decode_jwt(token)
        return Response({'valid': valid, 'message': message})

class ValidateTokenView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'bearer' or len(auth) != 2:
            return Response({'valid': False, 'message': 'No token provided'}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth[1]
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        payload, valid, message = decode_jwt(token)
        if not valid:
            return Response({'valid': False, 'message': message}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            'valid': True,
            'user': payload['username'],
            'expires': datetime.datetime.utcfromtimestamp(payload['exp']).replace(microsecond=0).isoformat() + 'Z'
        })
