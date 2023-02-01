from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'], 
            first_name = validated_data['first_name'], 
            last_name = validated_data['last_name'], 
            email = validated_data['email'], 
            age = validated_data['age'], 
            gender = validated_data['gender'], 
            password = validated_data['password1']
        )
        return user
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'age', 'gender']