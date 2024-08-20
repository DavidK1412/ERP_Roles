from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from securityApp.decorators import is_granted
from stockApp.models import Product
from stockApp.serializers import ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(is_granted('PRODUCT_DETAIL'))
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(is_granted('PRODUCT_UPDATE'))
    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @method_decorator(is_granted('PRODUCT_DELETE'))
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)