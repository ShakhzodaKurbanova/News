from django.contrib import admin
from .models import NewsCategory, News


@admin.register(NewsCategory)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id']
    list_display = ['name']


@admin.register(News)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['news_name']
    list_display = ['news_name']
