import jwt
from rest_framework import authentication, exceptions

from django.conf import settings

from .serializers import LoginDetailsSerializer
from .models import User


def is_Authenticated():
    return True


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, 'HS256')
            User.add_to_class("is_authenticated", is_Authenticated)
            user = User.objects.filter(email=payload['email']).first()
            return user, token
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')
        return super().authenticate(request)

