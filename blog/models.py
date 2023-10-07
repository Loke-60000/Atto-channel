from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Name of article', max_length=100, unique=True)
    text = models.TextField("Text")
    date = models.DateTimeField('date', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    #on_delete=CASCADE to delete all articles affilated with user

    views = models.IntegerField("Views", default=1)
    sizes = (
        ("A", 'Anonymous'),
        ("H", 'Hybrid'),
        ("P", 'Public'),
    )

    type_of_message = models.CharField(max_length=1, choices=sizes, default='P')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
# Create your models here.
