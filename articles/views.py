from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import DetailView, View, ListView

from articles.models import (
    Category, Article, ArticleScript, ArticleImage, CSS, JS, BrouserSupport)

class CategoryDetailView(DetailView):
    template_name = "articles/category_detail.html"
    model = Category
    context_object_name = 'curr_category'

    def get_context_data(self, **kwargs):
        category = self.get_object()
        context = super().get_context_data(**kwargs)
        context["children_categories"] = Category.objects.filter(
            parent=category, published=True)
        return context


class ArticleDetaileView(DetailView):
    template_name = "articles/article_detail.html"
    model = Article
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_obj = self.get_object()
        context["image_list"] = ArticleImage.objects.filter(
            atricle=article_obj)
        context["css_files"] = ArticleScript.objects.filter(
            script_type=CSS, atricle=article_obj)
        context["js_files"] = ArticleScript.objects.filter(
            script_type=JS, atricle=article_obj)
        context["brousers"] = BrouserSupport.objects.filter(
            atricle=article_obj)
        return context

class TestView(DetailView):
    template_name = "test.html"
    model = Article
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_obj = self.get_object()
        context["image_list"] = ArticleImage.objects.filter(
            atricle=article_obj)
        context["css_files"] = ArticleScript.objects.filter(
            script_type=CSS, atricle=article_obj)
        context["js_files"] = ArticleScript.objects.filter(
            script_type=JS, atricle=article_obj)
        context["brousers"] = BrouserSupport.objects.filter(
            atricle=article_obj)
        return context

class AutocomplitSearchView(View):

    def get(self, *args, **kwargs):
        search_str = self.request.GET.get("search_str", "")
        article_qs = Article.objects.filter(Q(
            title__icontains=search_str
        ) | Q(
            description__icontains=search_str
        ) | Q(
            category__title__icontains=search_str
        ))
        rendered = render_to_string('articles/ajax/search_list.html', context={
            "articles": article_qs
        })
        response = {'html': rendered}

        return JsonResponse(response)

class SearchResultView(ListView):
    template_name = "articles/search_page.html"
    context_object_name = "articles"

    def get_queryset(self, **kwargs):
        search_str = self.request.GET.get("search_str", "")
        article_qs = Article.objects.filter(Q(
            title__icontains=search_str
        ) | Q(
            description__icontains=search_str
        ) | Q(
            category__title__icontains=search_str
        ))
        return article_qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_str'] = self.request.GET.get("search_str", "")
        return context
