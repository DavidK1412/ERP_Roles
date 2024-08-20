from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.models import Role
from authApp.models import User
from authApp.serializers import UserSerializer


class UserAssociateRoleView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_CAN_SET_ROLES'))
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        roles_to_add = request.data.get('roles', [])

        for role_id in roles_to_add:
            try:
                role = Role.objects.get(pk=role_id)
                user.roles.add(role)
            except Role.DoesNotExist:
                return Response({'error': f'Role with id {role_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)


        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
