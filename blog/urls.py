from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
router.register(r'categories', views.ArticleCategoriesViewSet)
router.register(r'authors', views.AuthorsViewSet)
router.register(r'tags', views.TagsViewSet)
router.register(r'articles', views.ArticleListsViewSet)
router.register(r'article-tags', views.ArticleTagsViewSet)
router.register(r'article-images', views.ArticleImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('articles-detail/<slug:slug>', views.ArticleDetailBySlugView.as_view(), name="article-detail-by-slug"),
    path('hello/', views.hello, name='hello'),
]