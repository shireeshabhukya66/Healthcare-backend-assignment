from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        name = validated_data.pop('name')
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(
            username=email,
            first_name=name,
            email=email,
            password=password
        )

        return user