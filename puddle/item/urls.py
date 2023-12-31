from django.urls import path
from . import views

app_name='item'

urlpatterns = [
    path('<int:pk>/',views.detail,name='detail'),
    path("items/", views.items, name="items"),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('new/',views.new_item,name='new-item'),
]
