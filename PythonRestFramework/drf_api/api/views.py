import random
from django.utils.crypto import get_random_string
from rest_framework import status,filters,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .serializers import UserSerializer,UserLoginSerializer,UserDetailsSerializer,PasswordChangeSerializer
from .models import User

@api_view(['POST'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Generate Token
        token, created = Token.objects.get_or_create(user=user)

        # send welcome email
        subject = 'Welcome to CRUD API Test Page!'
        message = 'Welcome to Joining Us!.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [serializer.data['email']]
        send_mail(subject, message, email_from, recipient_list)

        # user details
        user_details_serializer = UserDetailsSerializer(user)

        # Return user details with token
        return Response({
            'user_details': user_details_serializer.data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Generate or get the token
            token, created = Token.objects.get_or_create(user=user)
            
            # Serialize user details
            user_details_serializer = UserDetailsSerializer(user)
            
            # Return user details with token
            return Response({
                'user_details': user_details_serializer.data,
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#User_Details
@api_view(['GET'])
def user_details(request):
    user = request.user
    serializer = UserDetailsSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

#User_List
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
    pagination_class = PageNumberPagination 

# Retrieve the profile of the authenticated user
    def get_object(self):
        return self.request.user 

#Edit_Page
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]
 # Retrieve the profile of the authenticated user
    def get_object(self):
        return self.request.user 
    
#Password_Updae

@api_view(['POST'])
def password_change(request):
    serializer = PasswordChangeSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')

        if not authenticate(username=user.email, password=old_password):
            return Response({'detail': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)  
            
        # Set and save new password
        user.set_password(new_password)
        user.save()
        
        return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Generate OTP
    otp = get_random_string(length=6, allowed_chars='0123456789')

    # Save the OTP
    user.reset_password_token = otp
    user.save()

    # Send the OTP to the user's email
    subject = 'Password Reset OTP'
    message = f'Your OTP for password reset is: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

    return Response({'detail': 'OTP sent successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_password(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    new_password = request.data.get('new_password')

    try:
        user = User.objects.get(email=email, reset_password_token=otp)
    except User.DoesNotExist:
        return Response({'detail': 'Invalid OTP or email'}, status=status.HTTP_400_BAD_REQUEST)

    # Reset the user's password
    user.set_password(new_password)
    user.reset_password_token = None
    user.save()

    return Response({'detail': 'Password reset successfully'}, status=status.HTTP_200_OK)

#LogOut
@api_view(['POST'])
def user_logout(request):
    try:
        # current token
        token = request.auth

        #delete_token
        token.delete()
        
        return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)