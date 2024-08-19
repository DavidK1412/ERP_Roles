from django.utils.decorators import method_decorator
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from authApp.utils import request_decode_token

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('AUTH_CAN_DETAIL_USERS', 'AUTH_DETAIL_OWN_USER'))
    def get(self, request, *args, **kwargs):
        valid_data = request_decode_token(request)
        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'detail':'Unauthorized Request'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)
