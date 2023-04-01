from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('signup', views.SignupView.as_view()),
    path('reset-password', views.PasswordResetView.as_view()),
]
