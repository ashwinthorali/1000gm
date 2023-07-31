from home.models import *

def allpage(request):
    event = Events.objects.filter(status=True).order_by('-id')
    ecat = ECategory.objects.all()
    vf =   LatestVideoFooter.objects.last()
    scoholastic = Scoholastic.objects.filter(status=True).order_by('-id')[:8]
    context = {
        'event':event,
        'vf':vf,
        'ecat':ecat,
        'scoholastic':scoholastic,
    }
    return context