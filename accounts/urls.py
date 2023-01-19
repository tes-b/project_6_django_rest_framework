from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register

urlpatterns = [
        path('login/', auth_view.LoginView.as_view(), name='login'), #로그인 
        path('logout/', auth_view.LogoutView.as_view(),name='logout'), #로그아웃
        path('register/', register, name='register')
]