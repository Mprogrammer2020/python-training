from django.shortcuts import render
from django.utils.crypto import get_random_string
from .models import CustomUser
from .serializers import UserSerializer,login_serializer,user_detalis,PasswordChangeSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Create your views here.

#user_signup

@api_view(['POST'])
def signup_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        #token
        token,created= Token.objects.get_or_create(user=user)
            
        # send mail
        subject = "TestPage"
        message = 'Welcome to Joining Us!.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [serializer.data['email']]
        send_mail(subject, message, email_from, recipient_list)
        
        return Response({"Detalis":serializer.data,"Token":token.key},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user_login

@api_view(['POST'])
def login_api(request):
    serializer = login_serializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password') 
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            
            user_serializer = UserSerializer(user)
            
            return Response({'user_details': user_serializer.data,'token': token.key }, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
@api_view()
def detalis_api(request):
    user=request.user
    Serializer=user_detalis(user) 
    return Response(Serializer.data, status=status.HTTP_200_OK)

#user_list

@api_view(['GET'])
def list_api(request):  
    search = request.query_params.get('search', None)
    queryset = CustomUser.objects.all()   
    if search:
        queryset = queryset.filter( Q(name__icontains=search) | Q(email__icontains=search))

    paginator = LimitOffsetPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)  
    serializer = user_detalis(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)

#update_profile

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
        serializer = user_detalis(request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
#update_password 
   
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def password_change(request):
    serializer = PasswordChangeSerializer(data=request.data)
    
    if serializer.is_valid():
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')
        user = request.user
        if not user.check_password(old_password):
           return Response({'detail': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#user_forget_password

@api_view(['POST'])

def forgot_password(request):
    email = request.data.get('email')
    users = CustomUser.objects.filter(email=email)

    if not users.exists():
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    user = users.first()
    otp = get_random_string(length=6, allowed_chars='0123456789')
    user.reset_password_token = otp
    user.save()

    subject = 'Password Reset OTP'
    message = f'Your OTP for password reset is: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

    return Response({'detail': 'OTP sent successfully'})


@api_view(['POST'])
def reset_password(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    new_password = request.data.get('new_password')

    if not email or not otp or not new_password:
        return Response({'detail': 'Email, OTP, and new password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(email=email, reset_password_token=otp)
    except CustomUser.DoesNotExist:
        return Response({'detail': 'Invalid OTP or email'}, status=status.HTTP_400_BAD_REQUEST)


    user.set_password(new_password)
    user.reset_password_token = None  
    user.save()

    return Response({'detail': 'Password reset successfully'}, status=status.HTTP_200_OK)

