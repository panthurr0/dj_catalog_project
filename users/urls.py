from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_verification, ChangePWView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<int:token>/', email_verification, name='email confirm'),
    path('change_password/', ChangePWView.as_view(), name='change_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
