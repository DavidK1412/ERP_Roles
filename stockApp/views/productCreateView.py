from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from stockApp.models import Product
from stockApp.serializers import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('PRODUCT_CREATE'))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
