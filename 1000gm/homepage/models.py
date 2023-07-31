from django.db import models

from home.models import BannerImage, EventBannerImage, AboutBannerImage


class BannerImageProxy(BannerImage):
    class Meta:
        proxy = True
        verbose_name='Banner Image'
        verbose_name_plural='Banner Image'


class EventBannerImageProxy(EventBannerImage):
    class Meta:
        proxy = True
        verbose_name='Homepage Event Content (max 3)'
        verbose_name_plural='Homepage Event Content (max 3)'

class AboutBannerImageProxy(AboutBannerImage):
    class Meta:
        proxy = True
        verbose_name='Homepage About Us Content (max 3)'
        verbose_name_plural='Homepage About Us Content (max 3)'
