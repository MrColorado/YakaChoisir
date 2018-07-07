from django.shortcuts import render
import datetime
import pytz
from database.models import Association
from django.http import HttpResponseRedirect
from database.views import base_views

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
        if e.date_begin > now and datetime.timedelta(days=30) + now >= aware >= now and e.validated:
            thirty.append(e)
        if cpt == 0 and e.premium and aware > now and e.validated:
            first.append(e)
            cpt = cpt + 1
            continue
        if e.validated and e.premium and cpt > 0 and aware >= now:
            events.append(e)
            numbers.append(cpt)
            cpt = cpt + 1
            continue

    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    '''if request.method == 'GET':
        search = request.GET.get('search_box')
        if search:
            res_event = Event.objects.filter(title=search)
            res_asso = Association.objects.filter(name=search)
            if len(res_event):
                return render(request, 'event/specific_event.html', {'res_event': res_event})
            if len(res_asso):
                asso = Association.objects.get(id=res_asso[0].id)
                return render(request, 'association/specific_association.html', {'res_asso': asso})'''

    return render(request, 'home/index.html', {'events': events, 'first': first, 'numbers': numbers, 'thirty': thirty})
