from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category

POSTS_ON_PAGE = 5


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )[:POSTS_ON_PAGE]
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=pk,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, template_name, context)
