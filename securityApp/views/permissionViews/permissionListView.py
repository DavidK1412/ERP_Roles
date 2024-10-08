from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.serializers.permissionSerializer import PermissionSerializer
from securityApp.models.permission import Permission


class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('PERMISSIONS_LIST_PERMISSIONS'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
