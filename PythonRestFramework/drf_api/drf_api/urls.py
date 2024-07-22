from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/crud/', include('api.urls')),  # Include app-level URLs for API endpoints
]
