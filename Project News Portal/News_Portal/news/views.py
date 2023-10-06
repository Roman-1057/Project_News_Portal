from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *

# класс для представления всех постов
class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'

    def post_sort(request):  # метод сортировки постов от новой даты к старой
        posts = Post.objects.order_by('-created_at')  # Сортировка по убыванию даты публикации

        context = {
            'news': posts,
        }

        return render(request, 'news.html', context)


class PostDetail(DetailView):  # класс отдельного поста
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def post_detail(request, pk):  # метод получения ссылки на страницу шаблона с этим постом (для перехода по ссылке на сайте)
        post = get_object_or_404(Post, pk)
        return render(request, 'news.html', {'post': post})
