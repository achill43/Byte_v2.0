from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from articles.utils import (
    generate_upload_image_path, generate_upload_script_path)


CSS = 'CSS'
JS = 'JS'

ARTICLE_SCRIPT_TYPE = (
    (CSS, 'CSS'),
    (JS, 'JavaScript'),
)

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("Slug"))
    icon = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Icon"))
    description = models.TextField(
        blank=True, null=True, verbose_name=_("Description"))
    published = models.BooleanField(
        default=True, verbose_name=_("If published"))
    parent = models.ForeignKey(
        'self', models.CASCADE, blank=True, null=True,
        verbose_name=_("Parent")
    )
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def get_publish_articles(self):
        return self.articles.all().filter(published=True).order_by("id")


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("Slug"))
    description = models.TextField(verbose_name=_("Description"))
    published = models.BooleanField(
        default=True, verbose_name=_("If published"))
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name=_("Category"), related_name="articles"
    )
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class ArticleImage(models.Model):
    atricle = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name=_("Article"))
    img_file = models.ImageField(
        upload_to=generate_upload_image_path, verbose_name=_("Image file"))
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)


class ArticleScript(models.Model):
    atricle = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name=_("Article"))
    script_file = models.FileField(
        upload_to=generate_upload_script_path, verbose_name=_("Script file"))
    script_type = models.CharField(
        max_length=3, choices=ARTICLE_SCRIPT_TYPE,
        verbose_name=_("Script type")
    )
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)


class Brouser(models.Model):
    title = models.CharField(max_length=20, verbose_name=_("Title"))
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Brouser')
        verbose_name_plural = _('Brousers')
        ordering = ["-id"]

class BrouserSupport(models.Model):
    brouser = models.ForeignKey(Brouser, on_delete=models.CASCADE)
    atricle = models.ForeignKey(Article, on_delete=models.CASCADE)
    support_version = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.brouser.title

    class Meta:
        verbose_name = _("Brouser Support")
        verbose_name_plural = _("Brousers Supports")
        ordering = ["-id"]
