"""mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from password_reset.urls import *
from django.core.mail.backends.console import EmailBackend
app_name = 'pwd_reset'
# app_name='article'
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r"^blog/",include('blog.urls',namespace='blog')),
    url(r"^account/",include('account.urls', namespace='account')),
    url(r'^pwd_reset/', include('password_reset.urls'),name ='pwd_reset'),
    #url(r'', include('password_reset.urls'),name ='pwd_reset'), #默认
    url(r"^article/",include('article.urls',namespace='article')),

]
