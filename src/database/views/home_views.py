from django.shortcuts import render
import datetime
import pytz

from database.models import Event

# Create your views here.

def home(request):
    events = []
    first = []
    thirty = []
    numbers = []
    allEvents = Event.objects.all()
    cpt = 0
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
    for e in allEvents:
        aware = datetime.datetime(e.date_begin.year, e.date_begin.month, e.date_begin.day, e.date_begin.hour,
                                e.date_begin.minute, e.date_begin.second, 0, pytz.UTC)
        if e.date_begin > now and datetime.timedelta(days=30) + now >= aware >= now:
            thirty.append(e)
        if cpt == 0 and e.premium and aware > now:
            first.append(e)
            cpt = cpt + 1
            continue
        if e.validated and e.premium and cpt > 0 and aware >= now:
            events.append(e)
            numbers.append(cpt)
            cpt = cpt + 1
            continue


    return render(request, 'home/index.html', {'events': events, 'first': first, 'numbers': numbers, 'thirty': thirty})


'''def searchBar(request):
    if request.method == 'POST' :
        e
    else :
        e

    return render(request, 'base.html')
'''