# Generated by Django 4.2.5 on 2023-10-07 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]