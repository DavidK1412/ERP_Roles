from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_CAN_DETAIL_USERS'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
