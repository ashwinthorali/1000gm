
from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('our-work/', views.our_work, name='our_work'),
    path('mission/', views.mission, name='mission'),
    path('past-events/', views.pevent, name='pevent'),
    path('upcoming-events/', views.uevent, name='uevent'),
    path('upcoming-events/<str:pk>/', views.ueventd, name='ueventd'),
    path('events/<str:pk>/', views.events_detail, name='events_detail'),
    path('calendar/', views.newcalendar, name='calendar'),
    # path('calendar-details/<str:pk>/', views.newcalendar, name='newcalendar'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:pk>/', views.blogs_detail, name='blogs_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('why-1000gm/', views.why, name='why'),
    path('1000gm-for-nms/', views.nms, name='nms'),
    path('1000gm-for-ims/', views.ims, name='ims'),
    path('1000gm-for-gms/', views.gms, name='gms'),
    path('donate/', views.donate, name='donate'),
    path('1000gm-for-parents/', views.parent, name='parent'),
    path('ways-to-help/', views.waystohelp, name='waystohelp'),
    path('coming-soon/', views.comingsoon, name='comingsoon'),
    path('our-team/', views.team, name='team'),
    
    path('chess-literacy/', views.scoholastic, name='scoholastic'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('chess-literacy-detail/<str:pk>/', views.scoholastic_detail, name='scoholastic_detail'),
    
    path('latest-videos/', views.latest_videos, name='latest_videos'),
    path('player-profile/', views.player_profile, name='player_profile'),
    path('press-release/', views.press_release, name='press_release'),
    path('press-release/<str:pk>/', views.press_release_detail, name='press_release_detail'),
] 
