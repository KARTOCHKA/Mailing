from django import forms

from blog.models import Post
from mailing.forms import FormStyleMixin


class PostForm(FormStyleMixin, forms.ModelForm):
    """Форма для создания поста в блоге"""
    class Meta:
        model = Post
        exclude = ('slug', 'is_published', 'count_of_view')
