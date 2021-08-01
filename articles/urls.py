from django.urls import path
from articles.models import Article

from articles import views

urlpatterns = [
    path(
        "categories/<slug:slug>/", views.CategoryDetailView.as_view(),
        name="category_detail"
    ),
    path(
        "articles/<slug:slug>", views.ArticleDetaileView.as_view(),
        name="article_detail"
    ),
    path(
        "ajax-search/", views.AutocomplitSearchView.as_view(),
        name="ajax_search"
    ),
    path(
        "search_page", views.SearchResultView.as_view(),
        name="search_page"
    )
]
