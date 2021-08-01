from modeltranslation import fields
from modeltranslation.translator import register, TranslationOptions

from articles.models import Category, Article, Brouser

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Brouser)
class BrouserTranslationsOprions(TranslationOptions):
    fields = ("title",)
