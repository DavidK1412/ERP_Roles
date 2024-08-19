from rest_framework import generics

from securityApp.models import Role
from securityApp.serializers.roleSerializer import RoleSerializer


class RoleDetailView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
