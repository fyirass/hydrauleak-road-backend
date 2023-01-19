from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from .serializers import SignupSerializer, UserSerializer

class SignupView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# class SigninView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = SigninSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(email=serializer.data['email'], password=serializer.data['password'])
#         if user:
#             login(request, user)
#             return Response(UserSerializer(user).data)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)