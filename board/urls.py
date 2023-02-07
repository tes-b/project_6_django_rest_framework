from django.urls import path
from . import views
app_name = 'board'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'),
    path('question/create/', views.question_create, name = 'question_create'),

    # API
    path('api/list/', views.BoardAPIView.as_view(), name = 'api/index'),
    path('api/create/', views.BoardCreateView.as_view(), name = 'api/create'),
    path('api/<int:pk>/', views.BoardDetailView.as_view(),  name = 'api/detail'),
    path('api/<int:pk>/answer/', views.AnswerCreateView.as_view(),  name = 'api/create/answer'),
    # path('api/<int:pk>/answer/<int:pk>', views.AnswerCreateView.as_view(),  name = 'api/delete/answer'),
]