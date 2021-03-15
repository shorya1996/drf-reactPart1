from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, LoginDetailsSerializer, LoginSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
import datetime
from django.conf import settings
import jwt


# Create your views here.


class SignupAPI(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email, password=password).first()
        if user:
            user = LoginDetailsSerializer(user)
            auth_token = jwt.encode({'email': user.data.get('email'), 'userid': user.data.get('userid'),
                                     'exp': datetime.datetime.timestamp(
                                         (datetime.datetime.now() + datetime.timedelta(days=1, hours=3)))},
                                    settings.SECRET_KEY, 'HS256')
            data = {
                'user': user.data, 'token': auth_token
            }
            return Response({'data': data, 'issuccess': True}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetails(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None, format=None):
        userid = pk
        if userid is not None:
            stu = User.objects.filter(userid=userid)
            serializer = LoginDetailsSerializer(stu, many=True)
            return Response({'data': serializer.data, 'isSuccess':True}, status=status.HTTP_200_OK)
        stu = User.objects.filter(userid=request.user.userid)
        serializer = LoginDetailsSerializer(stu, many=True)
        x = [dict(i) for i in serializer.data]
        return Response({'data': x, 'isSuccess':True}, status=status.HTTP_200_OK)


