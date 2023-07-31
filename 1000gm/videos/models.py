from django.db import models
from home.models import LatestVideo, VideoTestimonals, LatestVideoFooter
# Create your models here.

class LatestVideoProxy(LatestVideo):
    class Meta:
        proxy = True
        verbose_name='Latest Video'
        verbose_name_plural='Latest Videos'

class VideoTestimonalsProxy(VideoTestimonals):
    class Meta:
        proxy = True
        verbose_name='Video Testimonial'
        verbose_name_plural='Video Testimonials'

class LatestVideoFooterProxy(LatestVideoFooter):
    class Meta:
        proxy = True
        verbose_name='Footer Indisplay Video (max 1)'
        verbose_name_plural='Footer Indisplay Video (max 1)'