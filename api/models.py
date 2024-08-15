from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, date_of_birth=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=None, date_of_birth=None):
        user = self.create_user(email, password, name, date_of_birth)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = None  
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    reset_password_token = models.CharField(max_length=255, blank=True, null=True)
    reset_password_token_created_at = models.DateTimeField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
