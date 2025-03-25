from django.contrib import admin
from .models import Categories, News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

class NewsAd(admin.ModelAdmin):
    list_display = ['title', 'category', 'date']


admin.site.register(Categories, CategoryAdmin)

admin.site.register(News, NewsAd)
