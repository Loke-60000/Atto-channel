# Generated by Django 4.2.5 on 2023-10-15 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_threads_short'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
    ]