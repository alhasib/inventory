
from django.urls import path
from .views import * 

urlpatterns = [
    path('create-user/', create_user),
    path('add-permission', add_permission)
]