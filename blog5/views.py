from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Article, Category, Tag

class IndexView(generic.ListView):
    model = Article
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('created_at'),
            # 'counted_article': Article.objects.get(category_id=)
            'tag_list': Tag.objects.order_by('created_at'),
            # 'more_context': Category.objects.all(),
        })
        article_list = Article.objects.all().order_by('created_at')
        return context
    def get_queryset(self):
        return Article.objects.order_by('created_at')

class DetailView(generic.DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('created_at'),
            'article_list': Article.objects.all().order_by('created_at'),
            'tag_list': Tag.objects.order_by('created_at'),
            # 'prev_article': Article.objects.get(id={}),
            # 'next_article': Article.objects
            # 'more_context': Category.objects.all(),
        })
        return context
    def get_queryset(self):
        return Article.objects.order_by('created_at')


# Create your views here.
