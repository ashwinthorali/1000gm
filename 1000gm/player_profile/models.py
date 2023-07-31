from django.db import models
from home.models import PlayerProfile, PlayerProfileVideo
# Create your models here.

class PlayerProfileProxy(PlayerProfile):
    class Meta:
        proxy = True
        verbose_name='Player Profile'
        verbose_name_plural='Player Profile'


class PlayerProfileVideoProxy(PlayerProfileVideo):
    class Meta:
        proxy = True
        verbose_name='Player Videos'
        verbose_name_plural='Player Videos'


