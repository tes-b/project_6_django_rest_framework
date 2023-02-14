"""test_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from board import views
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="whdf_cp2",
        default_version="v1",
        description="API Documentation",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(name="test", email="test@test.com"),
        # license=openapi.License(name="Test License"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),


)



urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.index, name = 'index'),
    # restapi
    path('api-auth/', include('rest_framework.urls')),
    # dashboard
    path('dashboard/', include('dashboard.urls')),
    path('log/', include('log.urls')),
    # path('description/', schema_view_v1.with_ui('description', cache_timeout=0), name='description'),


]

