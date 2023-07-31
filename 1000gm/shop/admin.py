from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(CouponCodeUsage)
admin.site.register(CouponCode)
admin.site.register(Order)
admin.site.register(Products)