from zipfile import Path
from django.urls import path

from accounts.views import UserRegistrationView, UserLoginView, UserLogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
