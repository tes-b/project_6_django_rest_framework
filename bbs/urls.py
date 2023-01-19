from django.urls import path
from bbs import views

urlpatterns = [
    path('', views.list),
    path('bbs/write', views.write),
    path('bbs/list', views.list),

    # path('register/', views.register),
    # path('bbs/<article_id>',views.read),
    # path('getpostpage', views.getpostpage),
    # path('test/getpost', views.postdata),
]
