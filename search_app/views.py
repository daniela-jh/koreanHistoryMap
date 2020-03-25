from django.shortcuts import render
from khmap.models import Content
from django.db.models import Q

def searchResult(request):
    contents = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        queryStrip = query.strip()
        contents = Content.objects.all().filter(Q(locationName__contains=queryStrip) | Q(locationText1__contains=queryStrip) | Q(locationText2__contains=queryStrip) | Q(locationText3__contains=queryStrip) | Q(locationText4__contains=queryStrip))
        for content in contents:
            content.locationNameStr = content.locationName.replace(queryStrip, '<strong>' + queryStrip + '</strong>');
            content.locationText1Str = content.locationText1.replace(queryStrip, '<strong>' + queryStrip + '</strong>');
            content.locationText2Str = content.locationText2.replace(queryStrip, '<strong>' + queryStrip + '</strong>');
            content.locationText3Str = content.locationText3.replace(queryStrip, '<strong>' + queryStrip + '</strong>');
            content.locationText4Str = content.locationText4.replace(queryStrip, '<strong>' + queryStrip + '</strong>')

        return render(request, 'search_app/search.html', {'query':queryStrip, 'contents':contents})