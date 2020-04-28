from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('api/article/', ArticleList.as_view()),
    path('api/article/<int:pk>/', ArticleDetail.as_view()),
]
