from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']
           
    def create(self, validated_data):
        password = validated_data.pop('password',None) 
        instance = self.Meta.model(**validated_data) 
        if password is not None:
            instance.set_password(password)  
        instance.save()
        return instance    

        



class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()