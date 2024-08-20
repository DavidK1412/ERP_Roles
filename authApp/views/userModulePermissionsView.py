from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from authApp.models import User
from securityApp.models import Role, Permission, Module
from authApp.serializers import UserSerializer
from securityApp.serializers import PermissionSerializer
from securityApp.serializers import RoleSerializer


class UserModulePermissionsView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_CAN_SET_PERMISSIONS'))
    def get(self, request, pk_user, pk_module, *args, **kwargs):
        user = get_object_or_404(User, pk=pk_user)
        module = get_object_or_404(Module, pk=pk_module)
        module_permissions = module.permissions.all()
        user_permissions = user.user_permissions.all()
        roles = user.roles.all()

        user_module_permissions = []
        for user_permission in user_permissions:
            if user_permission in module_permissions:
                user_module_permissions.append(user_permission)

        role_module_permissions = []
        for role in roles:
            role_permissions = role.permissions.all()
            for role_permission in role_permissions:
                if role_permission in module_permissions:
                    role_module_permissions.append(role_permission)

        data = {
            "user": UserSerializer(user).data['username'],
            "module": module.name,
            "given_permissions": PermissionSerializer(user_module_permissions, many=True).data,
            "role_permissions": PermissionSerializer(role_module_permissions, many=True).data
        }

        return Response(data, status=status.HTTP_200_OK)
