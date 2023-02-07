
from django.urls import path
from .views import (
    index,
    detail,
    create
) 



urlpatterns = [
    path('', index),
    path('create/', create),
    path('<int:pk>/', detail),
    
]
