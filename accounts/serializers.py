from rest_framework import serializers
from .models import User
from .exceptions import CustomValidationError

from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status, generics


class SignUpSerializer(serializers.ModelSerializer):

    # 주석처리하니까 갑자기 됨...
    # email = serializers.EmailField(required=True)
    # username = serializers.CharField()
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()

    age = serializers.IntegerField()
    gender = serializers.CharField()
    password = serializers.CharField(
        required=True, write_only=True, style={'input_type': 'password'})
    password_check = serializers.CharField(
        required=True, write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        """
        회원가입 데이터 검증
        - 아이디 중복 체크
        - 비밀번호/비밀번호 확인 일치여부 검증
        """
        # FOR PROCESS CHECK >>
        # print("SignUpSerializer_validate") 
        # print("SignUpSerializer_validate_username : ", attrs['username'])
        # print("SignUpSerializer_validate_exist : ", User.objects.filter(username=attrs['username']).exists())
        # print("SignUpSerializer_validate_userall : ", User.objects.all())
        # << FOR PROCESS CHECK

        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username':'이미 존재하는 아이디입니다.'})

        if attrs['password'] != attrs['password_check']:
            raise serializers.ValidationError({'password':'비밀번호가 일치하지 않습니다.'})
        
        return attrs

    def create(self, validated_data):
        # password = validated_data.get('password')
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            password=validated_data['password'],
        )
        # user.set_password(password)
        # user.save()
        return user

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'password', 'password_check', 'first_name',
                  'last_name', 'email', 'age', 'gender']


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        user = authenticate(**data)
        if user:
            update_last_login(None, user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh = str(token)
            access = str(token.access_token)
            data = {
                'user': user.username,
                'refresh': refresh,
                'access': access,
            }
            return data

        raise CustomValidationError({"detail": "No active account found with the given credentials"}, 'username', status_code=status.HTTP_401_UNAUTHORIZED)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'