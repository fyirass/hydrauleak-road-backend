from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import UserSerializer

# class SignupView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request, format=None):
#         data = self.request.data

#         name = data['name']
#         email = data['email']
#         password = data['password']
#         password2 = data['password2']
        
#         is_leaker = data['is_leaker']
        
#         if is_leaker == 'True':
#             is_leaker = True
#         else:
#             is_leaker = False
            

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 return Response({'error': 'Email already exists'})
#             else:
#                 if len(password) < 6:
#                     return Response({'error': 'Password must be at least 6 characters'})
#                 else:
#                     user = User.objects.create_user(email=email, password=password, name=name)

#                     user.save()
#                     return Response({'success': 'User created successfully'})
#         else:
#             return Response({'error': 'Passwords do not match'})
   
   
   
   
   
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            

            if password == re_password:
                if len(password) >= 6:
                    if not User.objects.filter(email=email).exists():
                        
                        User.objects.create_user(name=name, email=email, password=password)

                        return Response(
                            {'success': 'User created successfully'},
                            status=status.HTTP_201_CREATED
                        )
                    
                    else:
                        return Response(
                            {'error': 'User with this email already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )