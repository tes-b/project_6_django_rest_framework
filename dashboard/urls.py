from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    # path('', views.index, name = 'index'),
    # path('dashboard/signed_public_dashboard/', views.signed_public_dashboard, name='signed_public_dashboard'),
    path('dashboard/signed_dashboard/', views.signed_dashboard, name = 'signed_dashboard'),
    # path('dashboard/signed_chart/', views.signed_chart, name = 'signed_chart')
]