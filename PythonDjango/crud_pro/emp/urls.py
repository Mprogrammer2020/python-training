from django.urls import path,include
from .views import signup, user_login, profile_list, user_detail, edit_profile, change_password, user_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profiles/', profile_list, name='profile_list'),
    path('profiles/<int:user_id>/', user_detail, name='user_detail'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('apii/',include('emp.api.urls'))

]
