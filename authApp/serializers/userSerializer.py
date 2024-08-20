from rest_framework import serializers
from authApp.models.user import User
from securityApp.models import Permission, Role


class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True
    )

    roles = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        many=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'permissions', 'roles']

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        roles_data = validated_data.pop('roles')
        user_instance = User.objects.create(
            **validated_data
        )
        for permission_data in permissions_data:
            user_instance.user_permissions.add(permission_data)
        for role_data in roles_data:
            user_instance.roles.add(role_data)
        return user_instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'permissions': {permission.id: permission.name for permission in instance.user_permissions.all()},
            'roles': {role.id: role.name for role in instance.roles.all()}
        }
