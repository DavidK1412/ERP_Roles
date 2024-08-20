from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from authApp.utils import request_decode_token

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_VIEW_PROFILE'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        valid_data = request_decode_token(self.request)
        return User.objects.get(id=valid_data['user_id'])
