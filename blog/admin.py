from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogArticles    #将BlogArticles类引入当前环境
# from .models import BlogArticlesAdmin
#
# #
# admin.site.register(BlogArticles)   #将类BlogArticles注册到ADMIN

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    list_filter = ("publish","author")
    search_fields = ("title","body")
    raw_id_fields = ("author",)  # 显示外键详细信息  (不能少 ,)
    date_hierarchy = "publish"
    ordering = ["publish","author"]

admin.site.register(BlogArticles,BlogArticlesAdmin)