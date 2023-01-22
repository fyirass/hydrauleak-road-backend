from rest_framework import viewsets, status
from .models import Report
from .serializers import ReportSerializer
from django.core.mail import send_mail
from rest_framework.decorators import action
from rest_framework.response import Response
from user.models import User
from email.mime.image import MIMEImage


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        report = serializer.save()
        self.send_report_email(report)

    @action(detail=False, methods=['post'])
    def send_report_email(self, report):
        subject = self.request.data.get('subject')
        message = self.request.data.get('message')
        add_sensor_coordinates = self.request.data.get('add_sensor_coordinates')
        add_mark_coordinates = self.request.data.get('add_mark_coordinates')
        add_pipe_coordinates = self.request.data.get('add_pipe_coordinates')
        add_pipe_access_coordinates = self.request.data.get('add_pipe_access_coordinates')
        report_date = self.request.data.get('report_date')
        image = self.request.data.get('image')
        
        
        try:
            admin = User.objects.filter(is_admin=True).first()
            admin_email = admin.email
        except User.DoesNotExist:
            admin_email = None
        
        
        message += '\n\nAdditional sensor coordinates: ' + str(add_sensor_coordinates)
        message += '\n\nAdditional mark coordinates: ' + str(add_mark_coordinates)
        message += '\n\nAdditional pipe coordinates: ' + str(add_pipe_coordinates)
        message += '\n\nAdditional pipe access coordinates: ' + str(add_pipe_access_coordinates)
        message += '\n\nReport date: ' + str(report_date)
        
        
        # with open(image.path, 'rb') as f:
        #     img_data = f.read()
        #     image = MIMEImage(img_data, name=image.name)
                    # .attach(image)
            
        if self.request.user.is_client:
            message ='Message from client: '+ message
            send_mail(subject, message, self.request.user.client.user.email, [admin_email])
        elif self.request.user.is_leaker:
            message ='Message from Leaker: '+ message
            send_mail(subject, message, self.request.user.leaker.user.email, [admin_email])
