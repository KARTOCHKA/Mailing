from django.conf import settings
from django.core.cache import cache

from blog.models import Post


def get_cache_detail_post():
    """Реализация низкоуровневого кеширования относительно одного поста в блоге"""
    queryset = Post.objects.all()
    if settings.CACHE_ENABLED:
        key = 'post_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = queryset
            cache.set(key, category_list)
        return category_list
    return queryset
