from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from accounts.views import user_list, user_create, signup


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/', views.signup, name = 'signup'),

    # 테스트용.. 추후 삭제 예정
    # path('api/user/', user_list.as_view()),
    # path('api/signup/', user_create.as_view())

]