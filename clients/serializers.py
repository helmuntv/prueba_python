from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Client
        fields = ['id','document', 'first_name', 'last_name', 'email', 'password','is_active']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ClientMassiveUploadSerializer(serializers.Serializer):
    file = serializers.FileField()