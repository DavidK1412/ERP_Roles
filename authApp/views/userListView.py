from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from authApp.models import User
from authApp.serializers import UserSerializer


class UserPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

    @method_decorator(is_granted('AUTH_CAN_LIST_USERS'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
