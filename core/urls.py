from leads.views import landing_page, LandingView
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    # path('', landing_page, name='landing-page'),
    path('', LandingView.as_view(), name='landing-page'), 
]
