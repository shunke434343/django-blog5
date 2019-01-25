from django.db import models
from django.utils import timezone
from tinymce import HTMLField
import datetime
import pytz


class Category(models.Model):
    category = models.CharField('カテゴリー', max_length=25)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField('タグ', max_length=25)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField('title', max_length=40)
    summary = models.CharField('summary', max_length=100, default="test")
    content = HTMLField('content', max_length=5000)
    image = models.ImageField(upload_to='documents/', default='defo')
    created_at = models.DateTimeField('date', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', default=11, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)

    def get_days_ago(self):
        now = datetime.datetime.now()
        timezone = pytz.timezone('Asia/Tokyo')
        now = timezone.localize(now)
        delta = now - self.created_at
        return delta.days

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField('コメント', max_length=300)
    name = models.CharField('名前', max_length=20, default="")
    mailadress = models.EmailField('メール', max_length=30, blank=True)
    article = models.ForeignKey(Article, verbose_name='親記事', on_delete=models.PROTECT, default=11)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.comment



# Create your models here.
