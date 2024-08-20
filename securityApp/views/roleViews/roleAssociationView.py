from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.models import Role, Permission
from securityApp.serializers import RoleSerializer


class RoleAssociationView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('ROLE_SET_PERMISSIONS'))
    def patch(self, request, *args, **kwargs):
        role = self.get_object()
        permissions_to_add = request.data.get('permissions', [])

        for permission_id in permissions_to_add:
            try:
                permission = Permission.objects.get(pk=permission_id)
                role.permissions.add(permission)
            except Permission.DoesNotExist:
                return Response({'error': f'Permission with id {permission_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        role.save()

        serializer = self.get_serializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)
