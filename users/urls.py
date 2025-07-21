from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
]
