from rest_framework import serializers
from authApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user_instance = User.objects.create(
            **validated_data
        )
        return user_instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username
        }
