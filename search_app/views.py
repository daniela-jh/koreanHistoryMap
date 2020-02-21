from django.shortcuts import render
from khmap.models import Content
from django.db.models import Q

def searchResult(request):
    contents = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        contents = Content.objects.all().filter(Q(locationName__contains=query) | Q(locationText1__contains=query) | Q(locationText2__contains=query) | Q(locationText3__contains=query) | Q(locationText4__contains=query))
        return render(request, 'search_app/search.html', {'query':query, 'contents':contents})