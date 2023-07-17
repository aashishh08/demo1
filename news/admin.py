from django.contrib import admin
from news.models import News

# Register your models here.

class News_admin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(News, News_admin)