# Generated by Django 5.1.7 on 2025-03-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_add_news_image_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_news',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
