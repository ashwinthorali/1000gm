from django.db import models
from home.models import Contact


class ContactProxy(Contact):
    class Meta:
        proxy = True
        verbose_name='Contact Form Data'
        verbose_name_plural='Contact Form Data'

class Newsletter(models.Model):
    updated  = models.DateField(auto_now=True)
    email = models.CharField(max_length = 156)

    def __str__(self):
        return self.email