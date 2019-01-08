#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:欣
@file: forms.py
@time: 2019/01/08
"""
from django import forms
from .models import ArticleColumn

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)