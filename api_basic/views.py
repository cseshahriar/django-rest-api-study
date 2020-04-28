from .models import Article
from django.shortcuts import render
from .serializers import ArticleSerializer

# from rest_framework.parsers import JSONParser
# from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# function base api view
@api_view(['GET', 'POST'])
def article_list(request):
    '''
    article list and create
    '''
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data) # 200 ok

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201 created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return from errors

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    '''
    Article detail and update, delete
    '''
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': # article read
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT': # article update
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200) # 200 ok
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': # article delete
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




