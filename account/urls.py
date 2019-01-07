#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:欣
@file: urls.py
@time: 2018/12/25
"""
from django.conf.urls import url
from . import views
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views

app_name="account"

urlpatterns = [
    # url(r"^login/$",views.user_login,name='user_login'),
    # url(r"^login/$",LoginView.as_view({"template_name":"registration/login.html"}),name='user_login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login1.html'), name='user_login'),
    url(r'^new-login/$',auth_views.LoginView.as_view(template_name ='account/login.html'),name='user_login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name ='account/logout.html'),name='user_logout'),
    url(r'^register/$',views.register,name='user_register'),
    url(r'^password-change/$',auth_views.PasswordChangeView.as_view(),name='password_change'),
    url(r'^password-change-done/$',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # url(r'^logout/$',auth_views.LogoutView.as_view(template_name ='registration/logged_out.html'),name='user_logout'),
    # auth 默认的转向地址
    # url(r'^logout/$',auth_views.LogoutView.as_view(),name='user_logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="account/password_reset_form.html",
        email_template_name="account/password_reset_email.html", success_url='/account/password-reset-done/'),
         name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",
         success_url='/account/password-reset-complete/'), name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    url(r'^myinformation/$',views.myself,name= 'my_information'),
    url(r'^edit-myinformation/$',views.myself_edit,name='edit_my_information'),
    url(r'^my-image/$',views.my_image,name="my_image"),

]

