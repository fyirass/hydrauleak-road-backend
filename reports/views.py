from rest_framework import viewsets, status
from .models import Report
from .serializers import ReportSerializer
from django.core.mail import send_mail
from rest_framework.decorators import action
from rest_framework.response import Response
from admins.models import Admin


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
        admin_email = Admin.objects.first().email
        message += '\n\nAdditional sensor coordinates: ' + str(add_sensor_coordinates)
        message += '\n\nAdditional mark coordinates: ' + str(add_mark_coordinates)
        message += '\n\nAdditional pipe coordinates: ' + str(add_pipe_coordinates)
        message += '\nAdditional pipe access coordinates: ' + str(add_pipe_access_coordinates)
        message += '\n\nReport date: ' + str(report_date)
        if self.request.user.is_client:
            send_mail(subject, message, self.request.user.client.email, [admin_email])
        elif self.request.user.is_leaker:
            send_mail(subject, message, self.request.user.leaker.email, [admin_email])

    # def perform_create(self, serializer):
    #     serializer.save()
    #     leaker = self.request.data.get('leaker')
    #     client = self.request.data.get('client')
    #     admin = self.request.data.get('admin')
        # subject = self.request.data.get('subject')
        # message = self.request.data.get('message')
        # add_sensor_coordinates = self.request.data.get('add_sensor_coordinates')
        # add_mark_coordinates = self.request.data.get('add_mark_coordinates')
        # add_pipe_coordinates = self.request.data.get('add_pipe_coordinates')
        # add_pipe_access_coordinates = self.request.data.get('add_pipe_access_coordinates')
        # report_date = self.request.data.get('report_date')

    #     if leaker:
    #         sender = "Leaker"
    #         sender_email = leaker.email
    #     elif client:
    #         sender = "Client"
    #         sender_email = client.email
    #     else:
    #         sender = "Unknown"
    #         sender_email = "from@example.com"

    #     admin_email = admin.email
    #     send_mail(
    #         'New Report Form Submission',
    #         f'Sender: {sender}\n Leaker: {leaker}\n Client: {client}\n Subject: {subject}\n Message: {message}\n Add_sensor_coordinates: {add_sensor_coordinates}\n Add_mark_coordinates: {add_mark_coordinates}\n Add_pipe_coordinates: {add_pipe_coordinates}\n Add_pipe_access_coordinates: {add_pipe_access_coordinates}\n Report_date: {report_date}',
    #         sender_email,
    #         [admin_email],
    #         fail_silently=False,
    #     )