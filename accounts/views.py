from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import UserForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, UserManager
from .serializers import UserSerializer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import generics

# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username = username, password = raw_password)  # 사용자 인증
#             login(request, user)  # 로그인
#             return redirect('index')
#     else:
#         form = UserForm()
#     return render(request, 'accounts/signup.html', {'form': form})

def signup(request):

    if request.method == 'GET':
        return render(request=request, template_name='accounts/signup.html')

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.POST)
        if user_serializer.is_valid():
            user_serializer.save()
        else :
            raise user_serializer.errors

        return redirect('index')


# 테스트용.. 추후 삭제 예정 by 태섭
# # @api_view(['GET'])
# class user_list(APIView):
#     def get(self, request):
#         queryset = User.objects.all()
#         print(queryset)
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

# # @api_view(['POST'])
# class user_create(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

