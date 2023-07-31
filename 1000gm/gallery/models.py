from django.db import models
from home.models import Gallery
class GalleryProxy(Gallery):
    class Meta:
        proxy = True
        verbose_name='Gallery'
        verbose_name_plural='Gallery'

