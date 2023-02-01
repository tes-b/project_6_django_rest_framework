from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# from accounts.views import signup


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/', views.SignUpAPIView.as_view(), name = 'signup'),

    # API
    path('api/login/',views.LogInGenericAPIView.as_view()),
    path('api/signup/',views.UserSignUpView.as_view()),
    path('api/<int:pk>/withdraw/',views.WithdrawalAPIView.as_view()),
    # path('api/login/', views.LogInGenericAPIView.as_view(), name='login')


]