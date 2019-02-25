from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Article, Category, Tag, Comment
from django.db.models import Q
from .forms import CommentCreateForm
import datetime

# トップページ
class IndexView(generic.ListView):
    model = Article
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('created_at'),
            'current_articles': Article.objects.order_by('-created_at'),
            'tag_list': Tag.objects.order_by('created_at'),
        })
        return context
    def get_queryset(self):
        queryset = Article.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword)|Q(content__icontains=keyword)
            )
        return queryset

# 記事の詳細ページ
class DetailView(generic.DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('created_at'),
            'article_list': Article.objects.all().order_by('-created_at'),
            'current_articles': Article.objects.order_by('-created_at'),
            'tag_list': Tag.objects.order_by('created_at'),
            'form': CommentCreateForm()
        })
        return context

# カテゴリー絞り込み
class CategoryView(generic.ListView):
    model = Article
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('created_at'),
            'current_articles': Article.objects.order_by('-created_at'),
            'tag_list': Tag.objects.order_by('created_at'),
        })
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Article.objects.order_by('-created_at').filter(category_id=category.id)
        return queryset

# タグ絞り込み
class TagView(generic.ListView):
    model = Article
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('created_at'),
            'current_articles': Article.objects.order_by('-created_at'),
            'tag_list': Tag.objects.order_by('created_at'),
        })
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        queryset = tag.article_set.all().order_by('-created_at')
        return queryset

def comment(request, article_id):
    form = CommentCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        article_pk = article_id
        comment = form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
        return redirect('blog5:detail', pk=article_pk)

    context = {
        'form':form
    }
    return render(request, 'root', context)
