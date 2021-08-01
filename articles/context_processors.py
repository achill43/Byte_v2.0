from articles.models import Category

def get_parent_categories(request):
    categories_qs = Category.objects.filter(
        published=True, parent=None).order_by("id")
    return {
        'categories': categories_qs
    }
