from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField("user Photo", default='kris.png', upload_to='user_images')

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = "Profiles"

class Rank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Implement different ranks later! PS. Your 4nmus
    rank = models.CharField(max_length=30, default='New user')

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
    class Meta:
        verbose_name = 'Rank'
        verbose_name_plural = "Ranks"
