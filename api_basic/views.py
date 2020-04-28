from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt

# function base api view
@csrf_exempt
def article_list(request):
    '''
    article list and create
    '''
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False, status=200) # 200 ok

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) # 201 created
        return JsonResponse(serializer.errors, status=404) # return from errors

@csrf_exempt
def article_detail(request, pk):
    '''
    Article detail and update, delete
    '''
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET': # article read
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, status=200) # 200 ok

    elif request.method == 'PUT': # article update
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200) # 200 ok
        return JsonResponse(serializer.errors, status=404) # return from errors

    elif request.method == 'DELETE': # article delete
        article.delete()
        return HttpResponse(status=204)




