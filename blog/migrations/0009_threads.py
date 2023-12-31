# Generated by Django 4.2.5 on 2023-10-10 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_alter_news_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Name of thread')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'Thread',
                'verbose_name_plural': 'Threads',
            },
        ),
    ]
