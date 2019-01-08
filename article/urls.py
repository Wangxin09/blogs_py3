#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:欣
@file: urls.py
@time: 2019/01/08
"""
from django.conf.urls import url
from . import views

app_name="article"
urlpatterns  = [
    url(r'^article-column/$',views.article_column,name='article_column')
]