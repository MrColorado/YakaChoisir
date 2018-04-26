from django.shortcuts import render
from database.models import Event
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


def specific_event(request, Myid):
    res_event = Event.objects.filter(id=Myid)
    if len(res_event):
        return render(request, 'events/specific_event.html', {'res_event': res_event})
    return render(request, 'not_found.html')

def create_event(request):
    if request.method == 'POST':
        form = createEventForm(request.POST)
        if form.is_valid():

            assoc_name = form.cleaned_data['association_name']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            place = form.cleaned_data['place']
            size_intern = form.cleaned_data['size_intern']
            size_extern = form.cleaned_data['size_extern']
            date_begin = form.cleaned_data['date_begin']
            date_end = form.cleaned_data['date_end']
            date_deadline = form.cleaned_data['date_deadline']
            photo = form.cleaned_data['photo']



            creer = True;

    else:
        form = createEventForm()

    assos = Association.objects.all();
    return render(request, 'create_event/create_event.html', locals(), {'assos': assos})
