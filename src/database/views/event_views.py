from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from database.models import Event, myUser
from database.models import Attend
from database.models import Association
from database.forms import createEventForm

import smtplib
from django.core.mail import send_mail

def event(request):
    events = []
    allEvents = Event.objects.all()
    for e in allEvents:
        if e.validated:
            events.append(e)
    return render(request, 'event/page_event.html', {'events': events})


def specific_event(request, event_id):
    res_event = Event.objects.filter(id=event_id)
    if len(res_event):
        return render(request, 'event/specific_event.html', {'res_event': res_event})
    return render(request, 'not_found.html')


@login_required
def my_event(request):
    events = []
    my_user = myUser.objects.get(user=request.user)
    event_id = Attend.objects.filter(user_id=my_user)
    for e in event_id:
        if e.event_id.date_begin > timezone.now():
            events.append(e.event_id)
    return render(request, 'event/my_event.html/', {'my_event': events})


@login_required
def register(request, current_event):
    my_event = Event.objects.get(id=current_event)
    my_user = myUser.objects.get(user=request.user)

    if Attend.objects.filter(event_id=my_event, user_id=my_user):
        return render(request, "event/register.html", {'res_event': None})

    new_attend = Attend(user_id=my_user,
                        event_id=my_event,
                        date_entry=timezone.now(),
                        ticket_number="test")
    new_attend.save()


    obj = "[inscription]" + my_event.title
    message = ""
    send_mail(
        obj,
        message,
        'event@epita.fr',
        [my_user.user.email],
        fail_silently=False,
    )
    return render(request, "event/register.html", {'res_event': my_event})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = createEventForm(request.POST)
        assoc_name = form.data['association_name']
        title = form.data['title']
        description = form.data['description']
        price = form.data['price']
        place = form.data['place']
        size_intern = form.data['size_intern']
        size_extern = form.data['size_extern']
        date_begin = form.data['date_begin']
        date_end = form.data['date_end']
        date_deadline = form.data['date_deadline']
        photo = form.data['photo']
        assoc = Association.objects.get(id=assoc_name)
        newEvent = Event(association_id=assoc,
                         title=title,
                         date_begin=date_begin,
                         date_end=date_end,
                         date_deadline=date_deadline,
                         validated=True,
                         description=description,
                         price=price,
                         place=place,
                         photo=photo,
                         size_intern=size_intern,
                         size_extern=size_extern)
        newEvent.save()
        creer = True
    else:
        form = createEventForm()
    assos = Association.objects.all()
    return render(request, 'event/create_event.html', locals(), {'assos': assos})


