from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserSerializer
from .permissions import IsAdminUser

from django.contrib.auth import get_user_model
User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        try:
            data = request.data
            
            phone = data['phone']
            name = data['name']
            email = data['email']
            
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            

            if password == re_password:
                if len(password) >= 6:
                    if not User.objects.filter(email=email).exists():
                        
                        User.objects.create_user(name=name, email=email, password=password, phone=phone)

                        return Response({
                                'user_id': User.objects.get(email=email).id,
                                'name': User.objects.get(email=email).name,
                                'email': User.objects.get(email=email).email,
                                'phone': User.objects.get(email=email).phone,
                                'is_admin': User.objects.get(email=email).is_admin,
                                'is_leaker': User.objects.get(email=email).is_leaker,
                                'is_client': User.objects.get(email=email).is_client
                            }, status=status.HTTP_201_CREATED)
                        
                        
                    
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

            

class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)