from leads.views import LandingView, SignUpView
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    path('', LandingView.as_view(), name='landing-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'), 
]
