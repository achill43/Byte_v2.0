from django.contrib import admin

try:
    from modeltranslation.admin import (
        TabbedDjangoJqueryTranslationAdmin as TranslationsAdmin
    )
except ModuleNotFoundError:
    from django.contrib.admin import ModelAdmin as TranslationsAdmin

from articles.forms import ArticleForm
from articles.models import (
    Category, Article, BrouserSupport, ArticleImage, ArticleScript,
    Brouser
)


@admin.register(Category)
class CategoryAdmin(TranslationsAdmin):
    list_display = ['title', 'published', 'parent', 'created_at']
    search_fields = ['title']
    list_filter = ['parent', 'published']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        models = Category

@admin.register(Brouser)
class BrouserAdmin(TranslationsAdmin):
    list_display = ['title', 'created']
    search_fields = ['title']


class ArticleImageTabularInline(admin.TabularInline):
    model = ArticleImage
    extra = 1


class ArticleScriptTabularInline(admin.TabularInline):
    model = ArticleScript
    extra = 1


class BSTabularInline(admin.TabularInline):
    model = BrouserSupport
    extra = 6


@admin.register(Article)
class ArticleAdmin(TranslationsAdmin):
    list_display = ['id', 'title', 'category', 'published', 'created_at']
    list_filter = ['category', 'created_at', 'published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    # form = ArticleForm
    inlines = [
        ArticleImageTabularInline,
        ArticleScriptTabularInline,
        BSTabularInline
    ]
