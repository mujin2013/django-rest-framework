#i!/usr/bin/env python
# -*- coding:utf-8 -*- 

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt    #因为我们需要POST数据，到这个视图的客户端，并没有CSRF令牌（token），所以我们需要为该视图标记为 csrf_exempt 
def snippet_list(request):
    """
    @description: 列出所有的代码片段或创建一个新的代码片段
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)    #将querySet进行序列化
        return JsonResponse(serializer.data, safe=False)    #safe若设置为False,那么第一个参数可以是任何可被JSON序列化的对象（https://docs.djangoproject.com/en/2.0/ref/request-response/#jsonresponse-objects）
    elif request.method == 'POST':
        data = JSONParser().parse(request)    #将request解析成python的原生数据类型
        serializer = SnippetSerializer(data=data)    #将原生数据类型，还原到一个被填充完毕的对象实例中
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    @description: 获取、更新、删除一个代码片段
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)    #对模型实例进行序列化
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



