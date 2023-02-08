from leads.views import LandingView
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    path('', LandingView.as_view(), name='landing-page')
]
