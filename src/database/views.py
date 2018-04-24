from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html')


def user_settings(request):
    return render(request, 'user_settings/user_settings.html')


def event(request):
    return render(request, 'event/event.html')

def specific_event(request):
    return render(request, 'events/specific_event.html')

def event(request):
    events = Event.objects.all()
    return render(request, 'page_defilante/page_defilente.html', {'events': events})