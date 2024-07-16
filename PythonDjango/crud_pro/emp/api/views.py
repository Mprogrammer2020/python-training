from emp.models import CustomUser
from emp.api.serializers import CustomUserSerializer,LoginSerializer,LogoutSerializer,PasswordChangeSerializer
from rest_framework import viewsets,filters,generics, permissions, status
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'date_of_birth']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name = self.request.query_params.get('name', None)
        search_email = self.request.query_params.get('email', None)
        
        if search_name:
            queryset = queryset.filter(username__icontains=search_name)
        if search_email:
            queryset = queryset.filter(email__icontains=search_email)
        
        return queryset

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.get_object()
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignupAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
#user login form
class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserPasswordChangeAPIView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')

        # Authenticate user with current password
        if not authenticate(username=user.email, password=old_password):
            return Response({'error': 'Invalid old password'})

        # Set and save new password
        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password changed successfully'})

class UserLogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return LogoutSerializer

    def get(self, request):
        logout(request)  
        serializer_class = self.get_serializer_class()
        serializer = serializer_class() 
        return Response(serializer.data)