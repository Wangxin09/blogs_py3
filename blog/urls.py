#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:欣
@file: urls.py
@time: 2018/12/23
"""
from django.conf.urls import url
from . import views

app_name="blog"
urlpatterns = [
    url(r"^$",views.blog_title,name="blog_title"),
    url(r'(?P<article_id>\d)/$', views.blog_article,name="blog_detail" ),
    # url(r'^article/(?P<article_id>[0-9]+)$', views.article_page),
]