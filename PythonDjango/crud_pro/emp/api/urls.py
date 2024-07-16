from django.urls import path,include
from emp.api import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()

router.register('crud',views.UserViewSet, basename='user')
urlpatterns=[
    path('',include(router.urls)),
    path('signup/', views.UserSignupAPIView.as_view(), name='signup'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
    path('change-password/', views.UserPasswordChangeAPIView.as_view(), name='change-password'),
]