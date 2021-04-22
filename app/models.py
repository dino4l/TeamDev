from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
    def best(self):
        return self.order_by('-rating')[:5]

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=256, verbose_name='Nickname')
    birthday = models.DateField(verbose_name='Дата рождения', default=timezone.now)
    image = models.ImageField(default='default.png', upload_to='avatar/%Y/%m/%d',)
    rating = models.PositiveIntegerField(default=0, verbose_name="Рейтинг")

    objects = ProfileManager()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'