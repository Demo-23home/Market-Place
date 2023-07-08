from django.urls import path
from .views import new_conversation,inbox,detail
app_name='conversation'

urlpatterns = [
    path('',inbox,name='inbox'),
    path('new/<int:pk>/',new_conversation,name='new'),
    path('<int:pk>/',detail,name='detail'),
]
