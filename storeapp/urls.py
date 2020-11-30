
from django.urls import path
from .views import * 


urlpatterns = [
    path('create-user/', create_user),
    path('proposal/', proposal, name = 'all-proposal'),
    path('<name>/', caregory_wise_product, name = 'category_wise_product'),
    
]