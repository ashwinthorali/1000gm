
from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('logout', views.byebye, name='byebye'),
    path('login', views.login_user, name='login_user'),
    path('singup', views.singup, name='singup'),
    
    
] 
