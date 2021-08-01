from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from articles.models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("__all__")
        widgets = {
            'description': CKEditorUploadingWidget(
                config_name='admin_ckeditor'),
        }
