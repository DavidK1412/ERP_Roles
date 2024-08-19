from rest_framework import status, generics
from rest_framework.response import Response

from securityApp.serializers.permissionSerializer import PermissionSerializer
from securityApp.models.permission import Permission


class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def list(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
