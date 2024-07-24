from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Define a custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'date_of_birth', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)

# Register UserAdmin
admin.site.register(User, CustomUserAdmin)
