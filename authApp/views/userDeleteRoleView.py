from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from authApp.models import User
from authApp.serializers.userSerializer import UserSerializer
from securityApp.models import Role


class UserDeleteRoleView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_CAN_SET_ROLES'))
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        roles_to_delete = request.data.get('roles', [])

        for role_id in roles_to_delete:
            try:
                role = Role.objects.get(pk=role_id)
                user.roles.remove(role)
            except Role.DoesNotExist:
                return Response({'error': f'Role with id {role_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
