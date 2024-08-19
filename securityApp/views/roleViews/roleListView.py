from rest_framework import generics

from securityApp.models import Role
from securityApp.serializers.roleSerializer import RoleSerializer


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
