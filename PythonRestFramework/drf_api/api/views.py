from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings

@api_view(['get'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Send welcome email
        subject = 'Welcome to Our Platform'
        message = 'welcome joining us'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [serializer.data['email']]
        send_mail(subject, message, email_from, recipient_list)
        response_data = {
            'email': serializer.data['email'],
            'name': serializer.data['name'],
            'date_of_birth': serializer.data['date_of_birth']
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
