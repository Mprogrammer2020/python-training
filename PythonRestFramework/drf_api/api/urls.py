from django.urls import path
from .views import (
    UserProfileView,
    user_signup,
    UserListView,
    user_login,
    user_details,
    password_change,
    forgot_password,
    reset_password,
    user_logout,
)

urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('user_details/', user_details, name='user_details'),
    path('users_list/', UserListView.as_view(), name='users_list'),  
    path('edit_profile/', UserProfileView.as_view(), name='edit_profile'), 
    path('change_pass/', password_change, name='change_pass'),  
    path('password/forgot/', forgot_password, name='forgot_password'),  
    path('password/reset/', reset_password, name='reset_password'), 
    path('logout/', user_logout, name='user_logout'),  
 
]
