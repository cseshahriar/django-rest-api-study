from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleGenericListView, ArticleGenericDetailView

urlpatterns = [
    path('api/article/', ArticleList.as_view()),
    path('api/article/', ArticleList.as_view()),

    path('api/generic/article/', ArticleGenericListView.as_view()),
    path('api/generic/article/<int:pk>/', ArticleGenericDetailView.as_view()),
]
