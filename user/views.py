from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import responses
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, ForgotPasswordSerializer

# Create your views here.
User = user_get_model()
