from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import  UserProfiles

#error
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','birth','phone')
#     list_filter = ('phone',)
#
# admin.site.register(UserProfile,UserProfileAdmin)

class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')
    list_filter = ('phone',)

admin.site.register(UserProfiles,UserProfilesAdmin)