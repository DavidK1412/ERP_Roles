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
from stockApp import views as stock_views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', auth_views.UserCreateView.as_view()),
    path('users/', auth_views.UserListView.as_view()),
    path('user/profile/', auth_views.UserProfileView.as_view()),
    path('user/detail/<str:pk>/', auth_views.UserDetailView.as_view()),
    path('user/associate/role/<str:pk>/', auth_views.UserAssociateRoleView.as_view()),
    path('user/associate/permission/<str:pk>/', auth_views.UserAssociatePermissionView.as_view()),
    path('user/unassociate/role/<str:pk>/', auth_views.UserDeleteRoleView.as_view()),
    path('user/unassociate/permission/<str:pk>/', auth_views.UserDeletePermissionView.as_view()),
    path('user/module/permissions/<str:pk_user>/<str:pk_module>/', auth_views.UserModulePermissionsView.as_view()),
    path('permission/', security_views.PermissionCreateView.as_view()),
    path('permission/<str:pk>/', security_views.PermissionDetailView.as_view()),
    path('permissions/', security_views.PermissionListView.as_view()),
    path('role/', security_views.RoleCreateView.as_view()),
    path('role/<str:pk>/', security_views.RoleDetailView.as_view()),
    path('role/association/<str:pk>/', security_views.RoleAssociationView.as_view()),
    path('roles/', security_views.RoleListView.as_view()),
    path('module/', security_views.ModuleCreateView.as_view()),
    path('module/<str:pk>/', security_views.ModuleDetailView.as_view()),
    path('modules/', security_views.ModuleListView.as_view()),
    path('modules/associate/<str:pk>/', security_views.ModuleAssociateView.as_view()),
    path('stock/product/', stock_views.ProductCreateView.as_view()),
    path('stock/product/<str:pk>/', stock_views.ProductDetailView.as_view()),
    path('stock/products/', stock_views.ProductListView.as_view()),

]
