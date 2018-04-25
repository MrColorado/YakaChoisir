from django.shortcuts import render
from database.models import Event


# Create your views here.

def home(request):
    return render(request, 'home/index.html')


def user_settings(request):
    return render(request, 'user_settings/user_settings.html')


# def event(request):
#    return render(request, 'event/event.html')

def event(request):
    events = Event.objects.all()
    return render(request, 'page_event/page_event.html', {'events': events})


def specific_event(request, Myid):
    res_event = Event.objects.filter(id=Myid)
    #res_event = get_object_or_404(Event, Myid)
    return render(request, 'events/specific_event.html', {'res_event': res_event})