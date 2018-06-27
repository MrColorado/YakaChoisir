from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from database.models import Event, myUser
from database.models import Attend
from database.models import Association
from database.forms import createEventForm
from database.forms import modifyEventForm
from database.models import Members
import smtplib
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils import timezone
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from database.views import base_views

from database.models import AssociationsManager
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
import random
import uuid


def event(request):
    events = []
    allEvents = Event.objects.all()
    for e in allEvents:
        if e.validated:
            if e.date_begin >= timezone.now():
                events.append(e)
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    return render(request, 'event/page_event.html', {'events': events})


def specific_event(request, event_id):
    god = False
    if request.user.is_authenticated:
        if len(AssociationsManager.objects.filter(user_id=myUser.objects.get(user=request.user))):
            god = True
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    res_event = Event.objects.filter(id=event_id)
    if len(res_event):
        inscrit = False
        if request.user.is_authenticated:
            user = myUser.objects.get(user=request.user)
            if len(Attend.objects.filter(user_id=user, event_id=event_id)):
                inscrit = True
        return render(request, 'event/specific_event.html',
                      {'res_event': res_event, 'inscrit': inscrit, 'god': god})
    return render(request, 'not_found.html')


@login_required
def my_event(request):
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    my_user = myUser.objects.get(user=request.user)
    god = False
    if request.user.is_authenticated:
        if len(AssociationsManager.objects.filter(user_id=myUser.objects.get(user=request.user))):
            god = True

    events = []
    event_id = Attend.objects.filter(user_id=my_user)
    for e in event_id:
        if e.event_id.date_begin >= timezone.now():
            events.append(e.event_id)
    return render(request, 'event/my_event.html/',
                  {'my_event': events, 'god': god})


def generate_pdf(event, user, hash_ticket):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont('Helvetica', 20)
    p.drawString(25, 400, "Ticket d'entrée")
    p.setFont('Helvetica', 25)
    p.drawString(25, 350, event.title)

    logo_epita = ImageReader("http://localhost:8000/static/img/epita_logo.png")
    p.drawImage(logo_epita, 10, 10, mask='auto')

    data_qr = hash_ticket
    data_qr.replace(" ", "")

    myqr = ImageReader(
        "https://chart.googleapis.com/chart?cht=qr&chl=" + data_qr + "&chs=160x160&chld=L|0")
    p.drawImage(myqr, 100, 100, mask='auto')

    p.setFont('Helvetica', 10)
    p.drawString(0, 0,
                 "PDF generate at " + timezone.now().strftime('%Y-%b-%d'))
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


@login_required
def register(request, current_event):
    my_event = Event.objects.get(id=current_event)
    my_user = myUser.objects.get(user=request.user)
    if Attend.objects.filter(event_id=my_event, user_id=my_user):
        return render(request, "event/register.html", {'res_event': None})

    if my_event.price > 0:
        paypal_dict = {
            "business": my_event.boutique,#"yakachoisir@epita.fr",
            "amount": str(my_event.price),
            "currency_code": "EUR",
            "item_name": "Ticket Evenement EPITA",
            "invoice": my_user.user.email + my_event.title,
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": 'http://127.0.0.1:8000/inscription_after_pay/' + str(current_event),  # TODO use hash pour secure
            "cancel_return": 'http://127.0.0.1:8000',  # TODO mettre page erreur paiement
            "custom": "premium_plan",
            # Custom command to correlate to some function later (optional)
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        context = {"form": form}
        return render(request, "event/pay_event.html", context)
    else:
        new_attend = Attend(user_id=my_user,
                            event_id=my_event,
                            date_entry=timezone.now(),
                            ticket_number=str(uuid.uuid1()))
        new_attend.save()

        obj = "[inscription]" + my_event.title
        message = "<h1> Votre inscription à l'évènement est enregistrée </h1><br>"
        message += "Vous pourrez vous rendre à l'évènement avec le ticket transmit en " \
                   "pièce jointe soit imprimé soit présent sur votre téléphone <br>"
        pdf = generate_pdf(my_event, my_user, new_attend.ticket_number)

        msg = EmailMessage(obj, message, to=[my_user.user.email])

        msg.attach('ticket.pdf', pdf, 'application/pdf')

        msg.content_subtype = "html"
        msg.send()
        return render(request, "event/register.html", {'res_event': my_event})


def register_after_pay(request, current_event):
    my_event = Event.objects.get(id=current_event)
    my_user = myUser.objects.get(user=request.user)

    if Attend.objects.filter(event_id=my_event, user_id=my_user):
        return render(request, "event/register.html", {'res_event': None})
    new_attend = Attend(user_id=my_user,
                        event_id=my_event,
                        date_entry=timezone.now(),
                        ticket_number=str(uuid.uuid1()))
    new_attend.save()

    obj = "[inscription]" + my_event.title
    message = "<h1> Votre inscription à l'évènement est enregistrée </h1><br>"
    message += "Vous pourrez vous rendre à l'évènement avec le ticket transmit en " \
               "pièce jointe soit imprimé soit présent sur votre téléphone <br>"
    pdf = generate_pdf(my_event, my_user, new_attend.ticket_number)

    msg = EmailMessage(obj, message, to=[my_user.user.email])

    msg.attach('ticket.pdf', pdf, 'application/pdf')

    msg.content_subtype = "html"
    msg.send()
    return render(request, "event/register.html", {'res_event': my_event})


@login_required
def create_event(request):
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    if request.method == 'POST':
        form = createEventForm(request.POST, request.FILES)
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
        photo = request.FILES['photo']
        boutique = form.data['boutique'] #TODO
        token = form.data['token']
        assoc = Association.objects.get(id=assoc_name)
        newEvent = Event(association_id=assoc,
                         title=title,
                         date_begin=date_begin,
                         date_end=date_end,
                         date_deadline=date_deadline,
                         validated=True,
                         description=description,
                         price=price,
                         boutique=boutique,
                         place=place,
                         photo=photo,
                         size_intern=size_intern,
                         size_extern=size_extern,
                         token_staff=token
                         )
        newEvent.save()
        creer = True
    else:
        form = createEventForm()
    assos = Association.objects.all()
    return render(request, 'event/create_event.html', locals(),
                  {'assos': assos})


@login_required
def modify_event(request, event_id):
    god = False
    if request.user.is_authenticated:
        if request.user.is_authenticated and len(
                AssociationsManager.objects.filter(user_id=myUser.objects.get(user=request.user))):
            god = True
    if request.method == 'GET':
        something = base_views.search(request)
        if something:
            return something
    res_event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = modifyEventForm(request.POST, request.FILES, event=res_event)
        res_event.title = form.data['title']
        res_event.description = form.data['description']
        res_event.price = form.data['price']
        res_event.place = form.data['place']
        res_event.size_intern = form.data['size_intern']
        res_event.size_extern = form.data['size_extern']
        res_event.date_begin = form.data['date_begin']
        res_event.date_end = form.data['date_end']
        res_event.date_deadline = form.data['date_deadline']
        res_event.photo = request.FILES['photo']
        res_event.premium = form.data['prenium']
        res_event.save()
        creer = True
    else:
        form = modifyEventForm(request.GET, event=res_event)
    return render(request, 'event/change_event.html', locals(),
                  {'event_id': event_id, 'god': god})
