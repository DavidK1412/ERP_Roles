from rest_framework import serializers

from securityApp.models import Permission
from securityApp.models.role import Role
from securityApp.serializers.permissionSerializer import PermissionSerializer


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True
    )

    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions', 'created_at', 'updated_at']

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        role_instance = Role.objects.create(
            **validated_data
        )
        for permission_data in permissions_data:
            role_instance.permissions.add(permission_data)
        return role_instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'permissions': PermissionSerializer(instance.permissions.all(), many=True).data,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at
        }
