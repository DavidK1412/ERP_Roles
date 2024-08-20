from rest_framework import serializers

from securityApp.models.module import Module
from securityApp.models.permission import Permission
from securityApp.serializers.permissionSerializer import PermissionSerializer


class ModuleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True
    )

    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'permissions']

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        module_instance = Module.objects.create(
            **validated_data
        )
        for permission_data in permissions_data:
            module_instance.permissions.add(permission_data)
        return module_instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'permissions': PermissionSerializer(instance.permissions.all(), many=True).data
        }
