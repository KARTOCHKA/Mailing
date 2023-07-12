from random import sample
from django.views.generic import TemplateView
from blog.models import Post
from main.services import get_count_mailing, get_active_mailing, get_unique_clients


class IndexView(TemplateView):
    """Представление главной страницы сервиса"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = list(Post.objects.all())
        context['random_post'] = sample(all_posts, min(3, len(all_posts)))
        context['count_mailing'] = get_count_mailing()
        context['active_mailing'] = get_active_mailing()
        context['unique_clients'] = get_unique_clients()

        return context
