from rest_framework import serializers
from .models import User
from datetime import datetime
from rest_framework import serializers
import pytz



class UserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(required=True, write_only=True)
    created_to_show = serializers.SerializerMethodField()

    class Meta: 
        model = User
        fields = ('username', 'email', 'phone_number', 'created', 'created_to_show', 'confirm_password')
        
        extra_kwargs = {
            'password' : {'write_only': True},
        }

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('passwords must match')
            return data
    
    def get_created_to_show(self, obj):
        if obj.created:
            datetime_obj = datetime.fromtimestamp(obj.created, pytz.timezone('Asia/Tehran'))
            return datetime_obj
        return None


    def create(self, validated_data):
        del validated_data['confirm_password']
        validated_data['created'] = datetime.now().timestamp()
        print(validated_data['created'])
        return super().create(validated_data)
    

        