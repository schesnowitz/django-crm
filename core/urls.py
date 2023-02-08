from leads.views import landing_page
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
]
