from rest_framework import serializers
from .models import User




class UserRegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta: 
        model = User
        fields = ('phone_number', 'password', 'confirm_password')
        
        extra_kwargs = {
            'password' : {'write_only': True},
        }

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('passwords must match')
            return data


    def create(self, validated_data):
        del validated_data['confirm_password']
        return super().create(validated_data)