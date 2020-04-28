from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('api/article/', article_list),
    path('api/article/<int:pk>/', article_detail),
]
