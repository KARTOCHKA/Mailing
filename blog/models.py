from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    """Модель описывающая пост в блоге"""
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, verbose_name='Slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    count_of_view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def delete(self, *args, **kwargs):
        """Функция, делающая пост не активным"""
        self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.title}'

    def increase_count_of_view(self):
        """Увеличивает счетчик просмотров на 1"""
        self.count_of_view += 1
        self.save()

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ('title',)
