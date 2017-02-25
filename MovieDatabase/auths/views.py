# views.py
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from auths.models import User
from auths.serializers import UserLoginSerializer, UserRegisterSerializer


class UserLoginView(CreateAPIView):
    serializer_class = UserLoginSerializer

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']
                user = authenticate(username=email, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return Response({
                        'message': "Login successful"
                    }, status=status.HTTP_200_OK)
                else:
                    return Response(
                        data={'message': 'Username and Password does not match or'
                                         ' user has not been activated'
                              }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(data={'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']
                first_name = serializer.data['first_name']
                last_name = serializer.data['last_name']
                user = User.objects.create_user(email, password, first_name, last_name, is_active=True)
                response_data = {
                    'message': "User {} has been created".format(user.get_username())
                }
                return Response(data=response_data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(data="Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserLogoutView(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'logged out'}, status=status.HTTP_200_OK)
