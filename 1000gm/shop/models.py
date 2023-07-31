from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from gm.getusername import get_request

class Category(models.Model):
    category = models.CharField(max_length = 900)
    def __str__(self):
        return self.category        

class Tag(models.Model):
    tag = models.CharField(max_length = 900)
    def __str__(self):
        return self.tag        

# Create your models here.
class Products(models.Model):
    meta_description = models.CharField(max_length = 900)
    slug = models.CharField(max_length = 156,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    title = models.CharField(max_length = 156)
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    canonical = models.CharField(max_length = 900, default="https://1000gm.org/")
    order  = models.IntegerField(blank=True, null=True)
    
    sold_out = models.BooleanField(default=False)
    
    product_name  = models.CharField(max_length = 156,blank=True, null=True)
    
    sp = models.CharField(max_length = 156,blank=True, null=True)
    mrp = models.CharField(max_length = 156,blank=True, null=True)
    
    note = models.CharField(max_length = 156,blank=True, null=True)
    short_desc = models.TextField(max_length = 1156,blank=True, null=True)   
    
    category  = models.ManyToManyField(Category,blank=True, null=True)
    tag  = models.ManyToManyField(Tag,blank=True, null=True)
    
    single_piece = models.BooleanField(default=True)
    in_stock =  models.IntegerField(blank=True, null=True, default=1)
    
    review =  models.IntegerField(blank=True, null=True)
    discount =  models.IntegerField(blank=True, null=True)
    
    
    description = RichTextUploadingField(blank=True, null=True)
    addional_info = RichTextUploadingField(blank=True, null=True)
    created_on  = models.DateField(auto_now_add=True)
    updated_on  = models.DateField(auto_now=True)
    

    img1 = models.ImageField(upload_to="Product", blank=True, null=True)
    img1_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    img2 = models.ImageField(upload_to="Product", blank=True, null=True)
    img2_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    
    def cartitem(self):
        try:
            a = get_request().user   
            item = Cart.objects.filter(user=a, product=self.id).count()
            if item > 0:
                return True
            else:
                return False
        except:
            pass

        

    def cartitemCount(self):
        a = get_request().user   
        i = 0 
        item = Cart.objects.filter(user=a, product=self.id).count()
        if item > 0:
            q = Cart.objects.get(user=a, product=self.id)
            i = q.qty
            return i
        else:
            return i


    def cartitemID(self):
        try:
            a = get_request().user    
            item = Cart.objects.filter(user=a, product=self.id).count()
            if item > 0:
                q = Cart.objects.get(user=a, product=self.id)
                return q.qty
            else:
                return 'abc'        
        except:
            pass

    def __str__(self):
        return self.product_name



    
class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="product", on_delete=models.CASCADE)
    qty  = models.IntegerField(blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)
    


class CouponCode(models.Model):
    code = models.CharField(max_length=30)
    discount  = models.IntegerField(blank=True, null=True)
    times  = models.IntegerField(blank=True, null=True)
    max_sp_discount  = models.IntegerField(blank=True, null=True)
    one_user  = models.BooleanField()
    user = models.ForeignKey(User, related_name="CouponCodeuser", on_delete=models.CASCADE,blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)


class CouponCodeUsage(models.Model):
    user = models.ForeignKey(User, related_name="CouponCode_user", on_delete=models.CASCADE,blank=True, null=True)
    coupon  = models.ForeignKey(CouponCode, on_delete=models.CASCADE, null=True)
    
    used = models.BooleanField(default=False)
    date  = models.DateTimeField(auto_now_add=True)
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name="user_wishlist", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="product_wishlist", on_delete=models.CASCADE)
    qty  = models.IntegerField(blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=101)
    name = models.CharField(max_length=310)
    email = models.CharField(max_length=310)
    company_name = models.CharField(max_length=310,blank=True, null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=130)
    country = models.CharField(max_length=1100, default='INDIA')
    zip_code = models.CharField(max_length=130)
    coupon_code = models.CharField(max_length=1200, blank=True, null=True)
    discount =  models.CharField(max_length=200, blank=True, null=True)
    total_amount  = models.IntegerField( blank=True, null=True)
    bill = models.TextField(max_length=11130, null=True, blank=True)
    payment_method = models.CharField(max_length=11200, blank=True, null=True)
    paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=11200, blank=True, null=True)
    privacy_policy = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name