from django.urls import path
from bbs import views

urlpatterns = [
    path('list/', views.list),
    path('write/', views.write),
    path('read/<int:post_num>', views.read),
    path('delete/<int:post_num>', views.delete),
    path('update/<int:post_num>', views.update),

]
