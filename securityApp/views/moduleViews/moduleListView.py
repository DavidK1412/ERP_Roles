from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from securityApp.models import Module
from securityApp.serializers import ModuleSerializer


class ModuleListView(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('MODULE_LIST'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
