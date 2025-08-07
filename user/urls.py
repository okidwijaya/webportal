from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ForgotPasswordView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/forgot-password/', ForgotPasswordView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]