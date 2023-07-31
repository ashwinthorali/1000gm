from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ECategory(models.Model):
    category = models.CharField(max_length = 156)
    slug= models.CharField(max_length = 156,blank=True, null=True)
    def tot(self):
        return Blog.objects.filter(category=self.id).count()

    def totactive(self):
        return Calendar.objects.filter(ecategory=self.id, active=True).count()

    def totinactive(self):
        return Calendar.objects.filter(ecategory=self.id, active=False).count()        
    
    def __str__(self):
        return self.category
    

class Category(models.Model):
    category = models.CharField(max_length = 156)
    def tot(self):
        return Blog.objects.filter(category=self.id).count()
    
    def __str__(self):
        return self.category

class Tags(models.Model):
    tags = models.CharField(max_length = 156)
    def __str__(self):
        return self.tags    

class Author(models.Model):
    description = RichTextUploadingField()
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    fb =models.CharField(max_length = 156,blank=True, null=True)
    insta = models.CharField(max_length = 156, blank=True, null=True)
    linkedin = models.CharField(max_length = 156, blank=True, null=True)
    image  = models.ImageField(upload_to="SEO")
    def __str__(self):
        return self.name     
               
# Create your models here.
class Blog(models.Model):
    main3 = models.BooleanField(default=False)
    most_visited = models.BooleanField(default=False)
    status  = models.BooleanField(default=True)
    page_name = models.CharField(max_length = 1256,blank=True, null=True)
    
    h1  = models.CharField(max_length = 156)
    slug =models.CharField(max_length = 1256,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    description = models.CharField(max_length = 900)
    title = models.CharField(max_length = 156)
    breadcrumb = models.CharField(max_length = 156)
    canonical = models.CharField(max_length = 900, default="https://thegrandindianroute.com/")
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    updated  = models.DateField(auto_now=True)
    published  = models.DateField()
    content = RichTextUploadingField()
    active = True
    edits = RichTextUploadingField( blank=True, null=True)
    category = models.ManyToManyField(Category, null=True)
    tag  = models.ManyToManyField(Tags, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.h1




class Events(models.Model):
    status  = models.BooleanField(default=True)
    event_category  = models.ForeignKey(ECategory, blank=True, null=True, on_delete=models.CASCADE)
    
    h1  = models.CharField(max_length = 156)
    slug =models.CharField(max_length = 1256,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    description = models.CharField(max_length = 900)
    title = models.CharField(max_length = 156)
    breadcrumb = models.CharField(max_length = 156)
    canonical = models.CharField(max_length = 900, default="https://1000gm.org/")
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    
    ads  = models.ImageField(upload_to="Ads", blank=True, null=True)
    ads_link  =  models.CharField(max_length = 156, blank=True, null=True)
    content = RichTextUploadingField()
    
    category = models.CharField(max_length = 900,blank=True, null=True)
    label_for_location_1 = models.CharField(max_length = 900, default="Venue For")
    location1 = models.CharField(max_length = 900,blank=True, null=True)
    
    label_for_location_2 = models.CharField(max_length = 900, default="Venue For", blank=True, null=True)
    location2 = models.CharField(max_length = 900,blank=True, null=True)
    
    label_for_location_3 = models.CharField(max_length = 900, default="Venue For", blank=True, null=True)
    location3 = models.CharField(max_length = 900,blank=True, null=True)
    
    label_for_location_4 = models.CharField(max_length = 900, default="Venue For", blank=True, null=True)
    location4 = models.CharField(max_length = 900,blank=True, null=True)
    
    date = models.CharField(max_length = 900,blank=True, null=True)
    
    banner_day = models.CharField(max_length = 900,blank=True, null=True)
    banner_month = models.CharField(max_length = 900,blank=True, null=True)

    mail = models.CharField(max_length = 900,blank=True, null=True)
    phone = models.CharField(max_length = 900,blank=True, null=True)

    map_pin = models.CharField(max_length = 900,blank=True, null=True)


    updated  = models.DateField(auto_now=True)
    published  = models.DateField()
    content = RichTextUploadingField()
    active = True
    edits = RichTextUploadingField( blank=True, null=True)
    
    youtube_link =  models.CharField(max_length = 900,blank=True, null=True)


    def __str__(self):
        return self.h1


class Calendar(models.Model): 
    ecategory  = models.ForeignKey(ECategory, null=True, blank=True, on_delete=models.CASCADE)
    active  = models.BooleanField(default=True)
    name = models.CharField(max_length = 1156)
    venue = models.CharField(max_length = 1156)
    date = models.CharField(max_length = 1156)
    expected = models.CharField(max_length = 1156, blank=True, null=True)
    webpage = models.CharField(max_length = 1156, blank=True, null=True)
    registration =  models.CharField(max_length = 1156, blank=True, null=True)
    adv_entry = models.CharField(max_length = 1156, blank=True, null=True)
    parings = models.CharField(max_length = 1156, blank=True, null=True)
    masters = models.CharField(max_length = 1156, blank=True, null=True)
    order = models.IntegerField()
    
    def __str__(self):
        return self.name
   
class LatestVideo(models.Model):   
    name = models.CharField(max_length = 1156)
    link = models.CharField(max_length = 1156, blank=True, null=True)
    banner_day = models.CharField(max_length = 900,blank=True, null=True)
    banner_month = models.CharField(max_length = 900,blank=True, null=True)

    def __str__(self):
        return self.name
   
class PlayerProfile(models.Model):   
    image  = models.ImageField(upload_to="Player_Profile", blank=True, null=True)
    
    name = models.CharField(max_length = 1156)
    fide_rating = models.IntegerField()
    fide_id = models.CharField(max_length = 1156)
    tournament_played = RichTextUploadingField()
    federation = models.CharField(max_length = 900,blank=True, null=True)
    in_home_page  = models.BooleanField(default=False)
    video_url = models.CharField(max_length = 900,blank=True, null=True)
    
    def __str__(self):
        return self.name
   



class Faqpage(models.Model):   
    question = models.CharField(max_length = 1156)
    answer = RichTextUploadingField( blank=True, null=True)

    
    def __str__(self):
        return self.question
   

class PlayerProfileVideo(models.Model):   
    iframe = models.TextField()
     
    

    
    def __str__(self):
        return str(self.id)
   


class AboutPage(models.Model):
    description = models.CharField(max_length = 900)
    keyword = models.CharField(max_length = 156)
    title = models.CharField(max_length = 156)
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    canonical = models.CharField(max_length = 900, default="https://website.com/")
    
    why_choose_us_img = models.ImageField(upload_to="Page Data", blank=True, null=True)
    why_choose_us_img_1 = models.ImageField(upload_to="Page Data", blank=True, null=True)
    
    
    def __str__(self):
        return self.title




class Testimonials(models.Model):   
    image  = models.ImageField(upload_to="SEO")
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    review = models.TextField()
 
    def __str__(self):
        return self.name
   
class VideoTestimonals(models.Model):   
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156, default="Dentist")
    video  = models.FileField(upload_to="Testmonials", null=True)
    def __str__(self):
        return self.name
      

class EventsGallery(models.Model):   
    name = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    category = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
   
class Client(models.Model):   
    name = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    
    def __str__(self):
        return self.name


class Gallery(models.Model):   
    name = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    
    def __str__(self):
        return self.name

class LatestVideoFooter(models.Model):   
    name = models.CharField(max_length = 156)
    link  = models.CharField(max_length = 156)
    hastag = models.CharField(max_length = 156, null=True)
    desc  = models.TextField(null=True)
    date  = models.DateField(null=True)
    
    
    def __str__(self):
        return self.name

class BannerImage(models.Model):   
    name = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    
    def __str__(self):
        return self.name

class EventBannerImage(models.Model):   
    name = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    
    def __str__(self):
        return self.name

class AboutBannerImage(models.Model):   
    name = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    description  = models.TextField(blank=True, null=True)
    link = models.CharField(max_length = 1256,blank=True, null=True)
    def __str__(self):
        return self.name



class PR(models.Model):
    status  = models.BooleanField(default=True)
    
    h1  = models.CharField(max_length = 156)
    slug =models.CharField(max_length = 1256,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    description = models.CharField(max_length = 900)
    title = models.CharField(max_length = 156)
    breadcrumb = models.CharField(max_length = 156)
    canonical = models.CharField(max_length = 900, default="https://1000gm.org/")
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156, default="https://1000gm.org/")
    image  = models.ImageField(upload_to="SEO")
    updated  = models.DateField(auto_now=True)
    published  = models.DateField()
    content = RichTextUploadingField()
    active = True
    
    def __str__(self):
        return self.h1



class Contact(models.Model):   
    name = models.CharField(max_length = 1156)
    email = models.CharField(max_length = 1156)
    subject = models.CharField(max_length = 1156)
    phone = models.CharField(max_length = 115,null=True, blank=True)
    message  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    responsded  = models.BooleanField(default=False)
    feedback  = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
 

class Team(models.Model):   
    name = models.CharField(max_length = 1156)
    position = models.CharField(max_length = 1156)
    image = models.ImageField(upload_to="TEAM")
    email = models.CharField(max_length = 115,default='someone@1000gm.org')
    def __str__(self):
        return self.name
 


 # Create your models here.
class Scoholastic(models.Model):
    status  = models.BooleanField(default=True)
    h1  = models.CharField(max_length = 156)
    slug =models.CharField(max_length = 1256,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    description = models.CharField(max_length = 900)
    title = models.CharField(max_length = 156)
    breadcrumb = models.CharField(max_length = 156)
    canonical = models.CharField(max_length = 900, default="https://www.1000gm.org/")
    
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    updated  = models.DateField(auto_now=True)
    published  = models.DateField()
    
    
    content = RichTextUploadingField()
    
    edits = RichTextUploadingField( blank=True, null=True)
    
    def __str__(self):
        return self.h1


