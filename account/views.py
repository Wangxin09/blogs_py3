# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm,RegistrationForm,UserProfilesForm
#   装饰器函数，（参数）
from django.contrib.auth.decorators import login_required
from .models import UserProfiles,UserInfo
from  django.contrib.auth.models import User


def user_login(request):
    if request.method == 'Post':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 表单数据验证
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('Wellcome You,You Have been authenticate successfully')
            else:
                return HttpResponse('Sorry,You are username and password is not right. ')
        else:
            return HttpResponse('Invalid login')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, "account/login.html", {'form': login_form})


# def register(request):
#     if request.method == 'POST':
#         user_form = RegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return HttpResponse('successfully')
#         else:
#             return HttpResponse('sorry,your can not register.')
#     else:
#         user_form = RegistrationForm()
#         return render(request,'account/register.html',{'form':'user_form'})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfilesForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            # 保存用户注册信息后，同时在account_userinfo 数据库表中写入该用户的ID信息
            UserInfo.objects.create(user=new_user)
            return HttpResponse('successfully')
        else:
            return HttpResponse('sorry,your can not register.')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfilesForm()
        return render(request,'account/register1.html',{'form':user_form,'profile':userprofile_form})

@login_required(login_url='account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    #userprofiles = UserProfiles.objects.get(user=user)
    #userinfo = UserInfo.objects.get(user=user)
    # userprofile = UserProfiles.objects.get(user=request.user)
    # userinfo = UserInfo.objects.get(user =request.user)
    userprofile = UserProfiles.objects.get(user=request.user) if hasattr(request.user,
                                                                        'userprofiles') else UserProfiles.objects.create(
        user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,
                                                                  'userinfo') else UserInfo.objects.create(
        user=request.user)

    return render(request,'account/myself.html',{'user':user,'userinfo':userinfo,'userprofile':userprofile})

from django.http import HttpResponseRedirect
from .forms import UserProfilesForm,UserInfoForm,UserForm

@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)     #if hasattr(request.user,'user') else User.objects.create( username=request.user.username)
    userprofile = UserProfiles.objects.get(user=request.user) if hasattr(request.user,
                                                     'userprofiles') else UserProfiles.objects.create( user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,
                                                     'userinfo') else UserInfo.objects.create(user=request.user)
    #userprofile = UserProfiles.objects.get(user=request.user)
    #userinfo =UserInfo.objects.get(user=request.user)
    if request.method == 'Post':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfilesForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid()*userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd =userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])
            request.user.email = user_cd['email']
            # user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            # user.save()
            userinfo.save()
            userprofile.save()
            return HttpResponseRedirect('/account/edit-myinformation/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form =UserProfilesForm(initial={'birth':userprofile.birth,'phone':userprofile.phone})
        userinfo_form =UserInfoForm(initial={'school':userinfo.school,'company':userinfo.company,'profession':userinfo.profession,'address':userinfo.address,'aboutme':userinfo.aboutme})
        return render(request,'account/myself_edit.html',{'user_form':user_form,'userprofile_form':userprofile_form,'userinfo_form':userinfo_form})

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method=='POST':
        img =request.POST['img']
        userinfo =UserInfo.objects.get(user=request.user.id)
        userinfo.photo=img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request,'account/imagecrop.html')