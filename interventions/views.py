from django.shortcuts import render
from .models import Intervention
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ManageInterventionView(APIView):
    def get (self, request, format=None):
        pass
    def post(self, request):
        try:
            user = request.user

            if not user.is_leaker:
                return Response(
                    {'error': 'User does not have necessary permissions for creating this listing data'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            data = self.retrieve_values(data)
            
            # client = data['client']
            intervention_title = data['intervention_title']
            
            slug = data['slug']
            if Intervention.objects.filter(slug=slug).exists():
                return Response(
                    {'error': 'Intervention with this slug already exists'}
                )
            
            intervention_description = data['intervention_description']
            
            intervention_type = data['intervention_type']
            
            if intervention_type == 'HIGHT':
                intervention_type = 'Hight'
                
            elif intervention_type == 'SIMPLE':
                intervention_type = 'Simple'
            else : 
                intervention_type = 'PipeSearch'
                
            
            intervention_status = data['intervention_status']
            
            if intervention_status == 'NOTSTART':
                intervention_status = 'NotStart'
                
            elif intervention_status == 'PENDING':
                intervention_status = 'Pending'
            else : 
                intervention_status = 'Completed'
            
            intervention_date = data['intervention_date']
            
            address = data['address']
            city = data['city']
            zipcode = data['zipcode']
            state = data['state']
            
            is_published = data['is_published']
            if is_published == 'True':
                is_published = True
            else:
                is_published = False
            
            Intervention.objects.create(
                leaker= user.email,
                # client= client.name,
                slug = slug,
                intervention_title = intervention_title,
                intervention_description = intervention_description,
                
                intervention_type = intervention_type,
                intervention_status = intervention_status,
                               
                intervention_date = intervention_date,
                address = address,
                city = city,
                state = state ,
                zipcode = zipcode,
    
                is_published = is_published
            )

            return Response(
                { 'success': 'intervention created successfully'},
                status = status.HTTP_201_CREATED
            )

            
            
        except:
            return Response(
                {'error': 'Something went wrong when creating intervention'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            