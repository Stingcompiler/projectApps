# Generated by Django 5.1.7 on 2025-04-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_add_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40, unique=True)),
                ('first_visit', models.DateTimeField(auto_now_add=True)),
                ('last_visit', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
