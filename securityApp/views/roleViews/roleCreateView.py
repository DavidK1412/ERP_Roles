from rest_framework import status, views
from rest_framework.response import Response

from securityApp.serializers.roleSerializer import RoleSerializer


class RoleCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
