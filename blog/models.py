from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from PIL import Image

class Threads(models.Model):
    title = models.CharField("Name of thread", max_length=100, unique=True)
    short = models.CharField("Short name of thread", max_length=5, unique=True, null = True)
    description = models.TextField("Description", max_length=500, null=True)
    date = models.DateTimeField("Date", default=timezone.now)
    # only for registered users! (subject to change) Ps. 4nmus
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        return reverse('comment-add', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'


class News(models.Model):
    text = models.TextField("Text", max_length= 500)
    date = models.DateTimeField('date', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE,  null=True, blank=True)
    # Only for testing purposes. Chagne null=True later!  Ps. 4nmus
    thread = models.ForeignKey(Threads, verbose_name='thread', on_delete=models.CASCADE, null=True)
    img = models.ImageField("img", upload_to="posts_images", null=True, blank=True)
    rand_id = models.TextField("rand_id", null=True, blank=True, default=" ")

    def get_absolute_url(self):
        return reverse('threads-detail', kwargs={'pk': self.thread.pk})

    def __str__(self):
        return f'{self.pk}'

    def save(self, *args, **kwargs):
        super().save()
        try:
            image = Image.open(self.img.path)

            if image.height > 256 or image.width > 256:
                resize = (256, 256)
                image.thumbnail(resize)
                image.save(self.img.path)
        except:
            pass

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

class Replies(models.Model):
    text = models.TextField("Text", max_length= 500)
    date = models.DateTimeField('date', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, null=True, blank=True)

    original = models.ForeignKey(News, verbose_name='comment #', on_delete=models.CASCADE, null=True)
    thread = models.ForeignKey(Threads, verbose_name='thread', on_delete=models.CASCADE, null=True, blank=True)
    rand_id = models.TextField("rand_id", null=True, blank=True, default=" ")

    def get_absolute_url(self):
        return reverse('threads-detail', kwargs={'pk': self.original.thread.pk})

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
# Create your models here.
