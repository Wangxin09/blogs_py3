from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.contrib import admin
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)    #   CharField()类型
    author = models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)  #   ForeignKey()    外键  -对多
    body = models.TextField()
    publish = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ("-publish",)    #显示顺序

# class BlogArticlesAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "publish")
#     list_filter = ("publish", "author")
#     search_fields = ("title", "body")
#     raw_id_fields = ("author")
#     date_hierarchy = "publish"
#     ordering = ["publish", "author"]

    def __str__(self):
        return self.title

