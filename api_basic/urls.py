from django.urls import path, include
from .views import (
    ArticleList, ArticleDetail,
    ArticleGenericListView, ArticleGenericDetailView,
    ArticleViewSet, ArticleGenericViewSet,
    ArticleModelViewSet,
 )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'generic/article', ArticleGenericViewSet, basename='garticle')
router.register(r'article/', ArticleModelViewSet, basename='gmarticle')

urlpatterns = [
    path('api/viewset/', include(router.urls)),
    path('api/viewset/<int:pk>/', include(router.urls)),

    path('api/generic/model/viewset/', include(router.urls)),

    path('api/article/', ArticleList.as_view()),
    path('api/article/', ArticleList.as_view()),

    path('api/generic/article/', ArticleGenericListView.as_view()),
    path('api/generic/article/<int:pk>/', ArticleGenericDetailView.as_view()),
]
