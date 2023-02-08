
from django.urls import path
from .views import (
    index,
    detail,
    create, 
    update,
    delete,
    IndexView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView, 
    LeadDeleteView 
) 

app_name = 'leads'

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),

    # path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/', LeadDetailView.as_view(), name='detail'),

    # path('create/', create, name='create'),
    path('create/', LeadCreateView.as_view(), name='create'),

    # path('<int:pk>/update', update, name='update'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='update'),

    path('<int:pk>/delete', LeadDeleteView.as_view(), name='delete'),
    # path('<int:pk>/delete', delete, name='delete'), 
]
