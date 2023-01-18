from django.urls import path
from bbs import views

urlpatterns = [
    path('', views.index),
    path('write/', views.write),
    path('register/', views.register),
    path('read/<article_id>',views.read)
]
'123'