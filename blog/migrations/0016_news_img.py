# Generated by Django 4.2.5 on 2023-10-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/posts_images', verbose_name='Image'),
        ),
    ]
