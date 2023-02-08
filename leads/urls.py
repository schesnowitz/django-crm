
from django.urls import path
from .views import (
    IndexView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView, 
    LeadDeleteView 
) 

app_name = 'leads'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', LeadDetailView.as_view(), name='detail'),
    path('create/', LeadCreateView.as_view(), name='create'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='delete'),
]
