# Generated by Django 2.1.5 on 2019-01-22 19:36

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(max_length=5000, verbose_name='content'),
        ),
    ]