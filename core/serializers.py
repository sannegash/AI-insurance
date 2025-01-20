# serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name', 
            'birth_date', 'gender', 'postal_code', 'city', 'state', 
            'role', 'status'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
