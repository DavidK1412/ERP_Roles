from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted

from authApp.models import User
from authApp.serializers.userSerializer import UserSerializer
from securityApp.models import Permission


class UserDeletePermissionView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_CAN_SET_PERMISSIONS'))
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        permissions_to_delete = request.data.get('permissions', [])

        for permission_id in permissions_to_delete:
            try:
                permission = Permission.objects.get(pk=permission_id)
                user.user_permissions.remove(permission)
            except Permission.DoesNotExist:
                return Response({'error': f'Permission with id {permission_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
