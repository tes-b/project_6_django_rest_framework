from django.urls import path
from . import views
app_name = 'log'

urlpatterns = [
    path('', views.api_root),
    path('logs/', views.LogsView.as_view(), name='logs'),
]
