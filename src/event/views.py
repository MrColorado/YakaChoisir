from django.shortcuts import render

# Create your views here.
def event(request):
    return render(request, 'page_defilante/page_defilente.html')

def specific_event(request):
    return render(request, 'events/specific_event.html')
