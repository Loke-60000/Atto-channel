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
    NW = "NEW"
    AR = "ATTO_CHANNELER "
    WB = "Weeb"
    GW = "Grand Weeb"
    AA = "ADMIN"
    RANK_CHOICES = [
        (NW, "New"),
        (AR, "Atto channeler"),
        (WB, "Weeb"),
        (GW, "Grand weeb"),
        (AA, "@Admin@"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=15,choices=RANK_CHOICES, default=NW)

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

    def is_upperclass(self):
        return self.RANK_CHOICES in {self.NW, self.GW}

    class Meta:
        verbose_name = 'Rank'
        verbose_name_plural = "Ranks"
