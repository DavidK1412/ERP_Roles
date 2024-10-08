from rest_framework import status, views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.serializers.permissionSerializer import PermissionSerializer


class PermissionCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('PERMISSIONS_CREATE_PERMISSIONS'))
    def post(self, request, *args, **kwargs):
        serializer = PermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
