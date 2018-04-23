from django.shortcuts import render

# Create your views here.
def event(request):
    return render(request, 'page_defilante/page_defilente.html')