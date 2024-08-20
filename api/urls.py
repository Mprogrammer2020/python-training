from  django.urls import  path
from .views import (signup_api,login_api,detalis_api,list_api,update_profile,
                    forgot_password,password_change,reset_password,logout_api)

urlpatterns = [
    path('signup/',signup_api,name='signup'),
    path('login/',login_api,name='login'),
    path('details/',detalis_api,name='details'),
    path('list/',list_api,name='list_api'),
    path('update_profile/',update_profile,name='update_profile'),
    path('update_pass/',password_change,name='update_pass'),
    path('forget_pass/',forgot_password,name='forget_pass'),
    path('reset_pass/',reset_password,name='reset_pass'),
    path('logout/',logout_api,name='logout')
         
]


