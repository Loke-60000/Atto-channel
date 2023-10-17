from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rank(models.Model):
    NW = "New"
    AR = "ATTO_CHANNELER"
    WB = "Weeb"
    GW = "-Grand Weeb-"
    AA = "@ADMIN@"
    RANK_CHOICES = [
        (NW, "NW"),
        (AR, "AR"),
        (WB, "WB"),
        (GW, "GW"),
        (AA, "AA"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=15, choices=RANK_CHOICES, default=NW)

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

    def is_upperclass(self):
        return self.RANK_CHOICES in {self.NW, self.GW}

    class Meta:
        verbose_name = 'Rank'
        verbose_name_plural = "Ranks"
