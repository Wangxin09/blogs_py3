from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import ArticleColumn,ArticlePost
from  .forms import ArticleColumnForm,ArticlePostForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# @login_required(login_url='/account/login/')
# def article_column(request):
#     columns = ArticleColumn.objects.filter(user=request.user)
#     return render(request, 'article/column/article_column.html', {'columns':columns})
#设置栏目
@login_required(login_url='/account/login/')
@csrf_exempt    #装饰器 提交表单scrf问题的解决
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, "article/column/article_column.html",{"columns":columns,"column_form":column_form})

    if request.method == 'POST':
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user,column=column_name)
            return HttpResponse('1')

#修改栏目名称
@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def rename_article_column(request):
    column_name = request.POST['column_name']
    column_id = request.POST['column_id']
    try:
        line  =ArticleColumn.objects.get(id = column_id)
        line.column = column_name
        line.save()
        return HttpResponse('1')
    except:
        return HttpResponse('0')
#删除栏目
@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def del_article_column(request):
    column_id = request.POST['column_id']
    try:
        line  =ArticleColumn.objects.get(id = column_id)
        line.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')

#文章发布
@login_required(login_url='/account/login/')
@csrf_exempt
# @require_POST   #405
def article_post(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False),
                new_article.user = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse('1')
            except:
                return HttpResponse('2')
        else:
            return HttpResponse('3')
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return  render(request, 'article/column/article_posts.html', {'article_post_form':article_post_form, 'article_columns':article_columns})

#标题列表
@login_required(login_url='/account/login/')
def article_list(request):
    articles_list = ArticlePost.objects.filter(author=request.user)
    paginator = Paginator(articles_list,2)
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
    return  render(request, 'article/column/article_list.html', {'articles':articles,'page':current_page})

#查看文章
@login_required(login_url='/account/login/')
def article_detail(request,id,slug):
    article = get_object_or_404(ArticlePost,id=id,slug=slug)
    return  render(request, 'article/column/article_detail.html', {'article':article,})


#删除文章
@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def del_article(request):
    article_id = request.POST['article_id']
    try:
        article = ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')

#修改文章
@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def redit_article(request,article_id):
    if request.method=='GET':
        article_columns = request.user.article_column.all()
        article = ArticlePost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={'title':article.title})
        this_article_column = article.column
        return render(request,'article/column/redit_article.html',{'article':article,'article_columns':article_columns,'this_article_column':this_article_column,'this_article_form':this_article_form})
    else:
        redit_article = ArticlePost.objects.get(id=article_id)
        try:
            redit_article.column = request.user.article_column.get(id = request.POST['column_id'])
            redit_article.title = request.POST['title']
            redit_article.body = request.POST['body']
            redit_article.save()
            return HttpResponse('1')
        except:
            return HttpResponse('2')