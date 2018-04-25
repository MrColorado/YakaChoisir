from django.shortcuts import get_object_or_404
from django.shortcuts import render

from database.models import Event


def specific_event(request, Myid):
    res_event = Event.objects.filter(id=Myid)
    #res_event = get_object_or_404(Event, Myid)
    return render(request, 'events/specific_event.html', {'res_event': res_event})
