from django.urls import path
from bbs import views

urlpatterns = [
    path('list/', views.list),
    path('write/', views.write),
    path('read/<int:post_num>', views.read),
    path('delete/<int:post_num>', views.delete)

    # path('post/<post_num>', views.post),
    # path('register/', views.register),
    # path('bbs/<article_id>',views.read),
    # path('getpostpage', views.getpostpage),
    # path('test/getpost', views.postdata),
]
