"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls.conf import include
from django.views.generic import TemplateView

from articles.views import TestView


i18n_urls = (
    path('admin/', admin.site.urls),
    path(
        '',
        TemplateView.as_view(
            template_name='homepage.html',
        ),
        name='home_page'
    ),
    path(
        "test/<int:pk>/", TestView.as_view(),
        name="article_test"
    ),
    path(
        'test/',
        TemplateView.as_view(
            template_name='test.html',
        ),
        name='test_page'
    ),
    path("articles/", include("articles.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
)

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns.extend(i18n_patterns(*i18n_urls, prefix_default_language=False))

urlpatterns.extend(static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
