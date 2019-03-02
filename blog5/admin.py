from django.contrib import admin
from . models import Article, Category, Tag
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
