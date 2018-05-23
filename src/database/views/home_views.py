from django.shortcuts import render


from database.models import Event

# Create your views here.

def home(request):
    events = []
    first = []
    numbers = []
    allEvents = Event.objects.all()
    cpt = 0
    for e in allEvents:
        if cpt == 0:
            first.append(e)
        if e.validated and e.premium and cpt > 0:
            events.append(e)
            numbers.append(cpt)
        cpt = cpt + 1

    return render(request, 'home/index.html', {'events': events, 'first': first, 'numbers': numbers})
