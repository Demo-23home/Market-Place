



app_name='users'

from . import views as user_views
from django.urls import path

urlpatterns = [
    path('signup/',user_views.signup,name='signup'),
]
