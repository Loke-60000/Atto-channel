from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField("user Photo", default='kris.png', upload_to='user_images')

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = "Profiles"
