from rest_framework import serializers

from stockApp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'stock']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'stock': instance.stock
        }
