from rest_framework import status, views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.serializers.roleSerializer import RoleSerializer


class RoleCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('ROLE_CREATE'))
    def post(self, request, *args, **kwargs):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
