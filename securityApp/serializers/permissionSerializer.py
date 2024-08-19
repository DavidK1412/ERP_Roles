from rest_framework import serializers
from securityApp.models.permission import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'created_at', 'updated_at']

    def create(self, validated_data):
        permission_instance = Permission.objects.create(
            **validated_data
        )
        return permission_instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at
        }
