from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.models.permission import Permission
from securityApp.serializers.permissionSerializer import PermissionSerializer


class PermissionDetailView(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('PERMISSIONS_DETAIL_PERMISSIONS'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
