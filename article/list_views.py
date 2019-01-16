#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:欣
@file: list_views.py
@time: 2019/01/17
"""
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ArticleColumn, ArticlePost
# from .forms import CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Count

# import redis
from django.conf import settings

# r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


def article_titles(request, username=None):
    # if username:
    #     user = User.objects.get(username=username)
    #     articles_title = ArticlePost.objects.filter(author=user)
    #     try:
    #         userinfo = user.userinfo
    #     except:
    #         userinfo = None
    # else:
    #     articles_title = ArticlePost.objects.all()
    articles_title = ArticlePost.objects.all()
    paginator = Paginator(articles_title, 2)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    # if username:
    #     return render(request, "article/list/author_articles.html",
    #                   {"articles": articles, "page": current_page, "userinfo": userinfo, "user": user})
    return render(request, "article/list/article_titles.html", {"articles": articles, "page": current_page})

#查看文章
def article_detail(request,id,slug):
    article = get_object_or_404(ArticlePost,id=id,slug=slug)
    return  render(request, 'article/list/article_detail.html', {'article':article,})