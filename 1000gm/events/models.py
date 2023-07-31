from django.db import models
from home.models import ECategory, Events
# Create your models here.


class ECategoryProxy(ECategory):
    class Meta:
        proxy = True
        verbose_name='Event Category'
        verbose_name_plural='Event Category'

class EventsProxy(Events):
    class Meta:
        proxy = True
        verbose_name='All Events'
        verbose_name_plural='All Events'