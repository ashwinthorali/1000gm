from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-id')[:3]
    ev = Events.objects.filter(status=True).order_by('-id')[:3]
    test = VideoTestimonals.objects.all().order_by('-id')[:3]
    banner = BannerImage.objects.all().order_by('-id')
    evbanner = EventBannerImage.objects.all().order_by('id')[:3]
    abbanner = AboutBannerImage.objects.all().order_by('id')[:3]
    pp = PlayerProfile.objects.filter(in_home_page=True).order_by('id')[:3]
    
    context = {
        'blogs':blogs,
        'ev':ev,
        'test':test,
        'banner':banner,
        'evbanner':evbanner,
        'abbanner':abbanner,
        'pp':pp,
    }
    return render(request, 'index.html', context)



def scoholastic(request):
    data = Scoholastic.objects.filter(status=True).order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'scoholastic.html', context)


def scoholastic_detail(request, pk):
    data = Scoholastic.objects.get(slug=pk)
    rt = Scoholastic.objects.filter(status=True).order_by('-id')[:6]
    context = {
        'data':data,
        'rt':rt,
    }
    return render(request, 'new/scholastic_detail.html', context)


def events(request):
    context = {

    }
    return render(request, 'events.html', context)

def events_detail(request, pk):
    data = Events.objects.get(slug=pk)
    context = {
        'data':data,
    }
    return render(request, 'event_detail.html', context)

def our_work(request):
    data = OurWork.objects.all()
    context = {
        'ourwork':our_work
    }
    return render(request, 'our_work.html', context)


def newcalendar(request):
    data = Calendar.objects.all().order_by('order')
    context = { 
        'data':data,
    }
    return render(request, 'new/newcalender.html', context)


def calendar(request):
    data = ECategory.objects.all()  
    context = { 
        'data':data,
    }
    return render(request, 'calender.html', context)

def gallery(request):
    data = Gallery.objects.all().order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'gallery.html', context)


def about(request):
    data = Team.objects.all()[:4]
    context = {
        'data':data
    }
    return render(request, 'about.html', context)

def team(request):
    data = Team.objects.all()
    context = {
        'data':data
    }
    return render(request, 'team.html', context)



def why(request):
    return render(request, 'why.html')

def nms(request):
    return render(request, 'nms.html')

def ims(request):
    return render(request, 'ims.html')
def gms(request):
    return render(request, 'gms.html')
def parent(request):
    return render(request, 'parents.html')

def waystohelp(request):
    return render(request, 'waystohelp.html')

def comingsoon(request):
    return render(request, 'comingsoon.html')

def donate(request):
    return render(request, 'donation.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data is sent successfully')
            return redirect('home:contact')
    context = {
    }
    return render(request, 'contact.html', context)


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successfully')
            return redirect('home:home')
    context = {
    }
    return render(request, 'contact.html', context)


def blogs(request):
    data = Blog.objects.all().order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'blog.html', context)

def blogs_detail(request, pk):
    data = Blog.objects.get(slug=pk)
    rp = Blog.objects.all().order_by('-id')[:6]
    context = {
        'data':data,
        'rp':rp,
    }
    return render(request, 'blog_detail.html', context)


def pevent(request):
    data = Events.objects.filter(status=False)

    context = {
        'data':data,
    }
    return render(request, 'pevent.html', context)


def uevent(request):
    data = Events.objects.filter(status=True)

    context = {
        'data':data,
    }
    return render(request, 'uevent.html', context)


def ueventd(request,pk):
    e = ECategory.objects.get(slug=pk)
    data = Events.objects.filter(event_category=e, status=True)

    context = {
        'data':data,
    }
    return render(request, 'uevent.html', context)


def latest_videos(request):
    data = LatestVideo.objects.all()

    context = {
        'data':data,
    }
    return render(request, 'latest_videos.html', context)

def player_profile(request):
    if request.method == 'GET':
        q =request.GET.get('q')
        if q:
            pass
        else:
            q=''    
        data1 =  PlayerProfile.objects.filter(name__contains=q)
        if data1:
            pass
        else:
            data1 =  PlayerProfile.objects.all()   
        page = request.GET.get('page', 1)

        
        paginator = Paginator(data1, 8)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        ppvideo = PlayerProfileVideo.objects.all()
        context = {
            'data':data,
            'ppvideo':ppvideo,
        }
    else:
        data1 =  PlayerProfile.objects.all()

        page = request.GET.get('page', 1)

        
        paginator = Paginator(data1, 8)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        ppvideo = PlayerProfileVideo.objects.all()
        context = {
            'data':data,
            'ppvideo':ppvideo,
        }    
    return render(request, 'player_profile.html', context)


def press_release(request):
    data = PR.objects.all()

    context = {
        'data':data,
    }
    return render(request, 'press_release.html', context)

def press_release_detail(request, pk):
    data = PR.objects.get(slug=pk)
    rp = Blog.objects.all().order_by('-id')[:6]
    context = {
        'data':data,
        'rp':rp,
    }
    return render(request, 'press_release_detail.html', context)

def mission(request):
    
    context = {
    }
    return render(request, 'mission.html')
