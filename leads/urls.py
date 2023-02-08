
from django.urls import path
from .views import (
    index,
    detail,
    create, 
    update,
    delete
) 

app_name = 'leads'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('<int:pk>/update', update, name='update'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete', delete, name='delete'),
]
