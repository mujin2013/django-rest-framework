#i!/usr/bin/env python
# -*- coding:utf-8 -*- 

# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),   #^api-auth/可以换成任何你喜欢的路径（这个url一加，浏览器上就会显示登录、登出）
]
