# Generated by Django 4.2.5 on 2023-10-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_threads_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='threads',
            name='short',
            field=models.CharField(max_length=5, null=True, unique=True, verbose_name='Short name of thread'),
        ),
    ]