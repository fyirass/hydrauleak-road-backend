from rest_framework import permissions
from rest_framework.views import APIView
from .models import Report
from django.core.mail import send_mail
from rest_framework.response import Response

class ReportCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        
        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'info@hydrauleak.com',
                ['firas.mansour.pro@gmail.com'],
                fail_silently=False
            )
            
            report = Report(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            report.save()
            
            return Response({'success': 'Report sent successfully'})
        
        except:
            return Response({'error': 'Report failed to send'})
            


