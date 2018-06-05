from django.shortcuts import render
from django.utils import timezone


from database.models import Event

# Create your views here.

def home(request):
    events = []
    first = []
    numbers = []
    allEvents = Event.objects.all()
    cpt = 0
    for e in allEvents:
        if cpt == 0 and e.premium and e.date_begin > timezone.now():
            first.append(e)
            cpt = cpt + 1
            continue
        if e.validated and e.premium and cpt > 0 and e.date_begin > timezone.now():
            events.append(e)
            numbers.append(cpt)
            cpt = cpt + 1

    return render(request, 'home/index.html', {'events': events, 'first': first, 'numbers': numbers})
