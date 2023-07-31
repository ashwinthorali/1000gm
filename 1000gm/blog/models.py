from django.db import models

from home.models import Blog, Author, Tags, Category
# Create your models here.

class BlogProxy(Blog):
    class Meta:
        proxy = True
        verbose_name='1000gm Blog'
        verbose_name_plural='1000gm Blogs'


class AuthorProxy(Author):
    class Meta:
        proxy = True
        verbose_name='Blog Author'
        verbose_name_plural='Blog Authors'

class TagsProxy(Tags):
    class Meta:
        proxy = True
        verbose_name='Tags in Blog'
        verbose_name_plural='Tags in Blogs'

class CategoryProxy(Category):
    class Meta:
        proxy = True
        verbose_name='Category for Blog'
        verbose_name_plural='Category for Blogs'