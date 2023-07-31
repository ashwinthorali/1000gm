from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BlogProxy)
admin.site.register(TagsProxy)
admin.site.register(CategoryProxy)
admin.site.register(AuthorProxy)