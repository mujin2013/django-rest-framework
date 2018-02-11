#i!/usr/bin/env python
# -*- coding:utf-8 -*- 

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views


#创建路由器并将我们的viewset注册
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

#API的urls由我们的router自动确定
urlpatterns = [
    url(r'^', include(router.urls))
]

