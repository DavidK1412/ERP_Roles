"""
URL configuration for erpRoles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from securityApp import views as security_views
from authApp import views as auth_views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', auth_views.UserCreateView.as_view()),
    path('user/<str:pk>/', auth_views.UserDetailView.as_view()),
    path('permission/', security_views.PermissionCreateView.as_view()),
    path('permission/<str:pk>/', security_views.PermissionDetailView.as_view()),
    path('permissions/', security_views.PermissionListView.as_view()),
    path('role/', security_views.RoleCreateView.as_view()),
    path('role/<str:pk>/', security_views.RoleDetailView.as_view()),
    path('roles/', security_views.RoleListView.as_view()),
]
