from django.db import models
from django.utils import timezone
# from tinymce import HTMLField

# Create your views here.
class Article(models.Model):
    title = models.CharField('title', max_length=40)
    content = models.TextField('content', max_length=5000)
    created_at = models.DateTimeField('date', default=timezone.now)

class Category(models.Model):
    category = models.CharField('カテゴリー', max_length=25)
    created_at = models.DateTimeField('作成日', default=timezone.now)

class Tag(models.Model):
    tag = models.CharField('タグ', max_length=25)
    created_at = models.DateTimeField('作成日', default=timezone.now)
# Create your models here.
