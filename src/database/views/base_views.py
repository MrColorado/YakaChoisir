from django.shortcuts import render


from database.models import Association
from django.http import HttpResponseRedirect

from database.models import Event

def search(request):

    print("lol ca devrai marcher")
    if request.method == 'GET':
        search = request.GET.get('search_box')
        if search:
            res_event = Event.objects.filter(title=search)
            res_asso = Association.objects.filter(name=search)
            if len(res_event):
                return render(request, 'event/specific_event.html', {'res_event': res_event})
            if len(res_asso):
                asso = Association.objects.get(id=res_asso[0].id)
                return render(request, 'association/specific_association.html', {'res_asso': asso})
