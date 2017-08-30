# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from  django.template import loader
from .models import Album

"""
def index1(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums
    }
    return HttpResponse(template.render(context, request))
"""
# Combines Load and Render Function
def index(request):
    # return HttpResponse("<h1>This is the Music app homepage</h1>")
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    """ try:
            album = Album.objects.get(pk=album_id)
        except Album.DoesNotExist:
            raise Http404("Album Does Not Exists")"""
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

