from django.shortcuts import render
from database.models import Event, myUser
from database.models import Association
from database.forms import createEventForm


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


def specific_event(request, event_id):
    res_event = Event.objects.filter(id=event_id)
    if len(res_event):
        return render(request, 'events/specific_event.html', {'res_event': res_event})
    return render(request, 'not_found.html')


def create_event(request):
    if request.method == 'POST':
        form = createEventForm(request.POST)

        #print(form.errors)
        #if form.is_valid():

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

        creer = True;

    elif Association.objects.all().count() == 0:
        return render(request, 'not_found.html')
    else:
        form = createEventForm()

    assos = Association.objects.all();
    return render(request, 'create_event/create_event.html', locals(), {'assos': assos})


def user_information(request):
    if request.user.is_anonymous:
        return render(request, 'not_found.html')
    user_info = myUser.objects.get(user=request.user)
    return render(request, 'user_settings/user_settings.html', {'user_info': user_info})


