from rest_framework import generics

from securityApp.models.permission import Permission
from securityApp.serializers.permissionSerializer import PermissionSerializer


class PermissionDetailView(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
