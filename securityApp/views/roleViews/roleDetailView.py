from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.models import Role
from securityApp.serializers.roleSerializer import RoleSerializer


class RoleDetailView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('ROLE_DETAIL'))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
