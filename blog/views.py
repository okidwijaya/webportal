from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import RetrieveAPIView
from .models import (
    UserProfile, ArticleCategories, Authors, Tags,
    ArticleLists, ArticleTags, ArticleImages
)
from .serializers import (
    UserProfileSerializer, ArticleCategoriesSerializer, AuthorsSerializer, 
    TagsSerializer, ArticleListsSerializer, ArticleTagsSerializer, 
    ArticleImagesSerializer
)

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world! This is the blog app.")

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ArticleCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategories.objects.all()
    serializer_class = ArticleCategoriesSerializer

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class ArticleListsViewSet(viewsets.ModelViewSet):
    queryset = ArticleLists.objects.all()
    serializer_class = ArticleListsSerializer

class ArticleTagsViewSet(viewsets.ModelViewSet):
    queryset = ArticleTags.objects.all()
    serializer_class = ArticleTagsSerializer


class ArticleImagesViewSet(viewsets.ModelViewSet):
    queryset = ArticleImages.objects.all()
    serializer_class = ArticleImagesSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    
# class ArticleImagesViewSet(viewsets.ModelViewSet):
#     queryset = ArticleImages.objects.all()
#     serializer_class = ArticleImagesSerializer

class ArticleDetailBySlugView(RetrieveAPIView):
    queryset = ArticleLists.objects.all()
    serializer_class = ArticleListsSerializer
    lookup_field = 'slug'
