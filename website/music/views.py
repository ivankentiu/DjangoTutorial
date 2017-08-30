# from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    # return HttpResponse("<h1>This is the Music app homepage</h1>")
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exists")
    return render(request, 'music/detail.html', {'album': album})

