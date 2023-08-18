from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(PostListView.as_view()), name='home'),
    path('create/', PostCreateView.as_view(), name='blog_form'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
    path('form/', never_cache(PostCreateView.as_view()), name='blog_form'),
    path('update/<int:pk>/', never_cache(PostUpdateView.as_view()), name='blog_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='blog_confirm_delete')
]
