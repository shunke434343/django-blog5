# Generated by Django 2.1.5 on 2019-01-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog5', '0003_auto_20190123_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=30, verbose_name='メール'),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='名前'),
        ),
    ]
