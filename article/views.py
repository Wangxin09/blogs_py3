from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ArticleColumn
from  .forms import ArticleColumnForm
@login_required(login_url='/account/login/')
def article_column(request):
    columns = ArticleColumn.objects.filter(user=request.user)
    return render(request, 'article/column/article_column.html', {'columns':columns})

@login_required(login_url='/account/login/')
@csrf_exempt    #装饰器 提交表单scrf问题的解决
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, 'article/column/article_column.html', {'columns':columns, 'column_form':column_form})

    if request.method == 'POST':
        column_name = request.POST['COLUMN']
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user,column=column_name)
            return HttpResponse('1')