



app_name='users'
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.urls import path
from .forms import LoginForm


urlpatterns = [
    path('signup/',user_views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=LoginForm),name='login'),
]
