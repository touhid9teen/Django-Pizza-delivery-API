from enum import unique

from rest_framework import serializers
from authentication.models import User
# from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=25)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8)
    phone_number = serializers.CharField(max_length=20,allow_null=False, allow_blank=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number']


    def validate(self, data):
        username_exist = User.objects.filter(username=data['username']).exists()
        if username_exist:
            raise serializers.ValidationError('User already exists')
        email_exist = User.objects.filter(email=data['email']).exists()
        if email_exist:
            raise serializers.ValidationError('Email already exists')
        phone_number_exist = User.objects.filter(phone_number=data['phone_number']).exists()
        if phone_number_exist:
            raise serializers.ValidationError('Phone number already exists')

        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=25)
    password = serializers.CharField(min_length=8)

