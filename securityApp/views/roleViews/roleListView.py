from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.models import Role
from securityApp.serializers.roleSerializer import RoleSerializer


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('ROLE_LIST'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
