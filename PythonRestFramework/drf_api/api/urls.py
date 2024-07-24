from django.urls import path

from .views import UserProfileView,user_signup,UserListView,user_login,user_details,password_change

urlpatterns = [

    path('signup/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('user_details/', user_details, name='user_details'),
    path('users_list/', UserListView.as_view(), name='users'),  
    path('edit_profile/', UserProfileView.as_view(), name='edit_profile'),
    path('change_pass/',password_change, name="change_pas")

]




