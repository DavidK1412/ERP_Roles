from rest_framework import status, views
from rest_framework.response import Response

from securityApp.serializers.permissionSerializer import PermissionSerializer


class PermissionCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
