from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album
# Create your views here.
def index(resquest):
	all_albums = Album.objects.all()
	ctx = {'all_albums': all_albums}
	return render(resquest, 'web0/index.html', ctx)


def detail(resquest, album_id):
	try:
		album = Album.objects.get(id=album_id)
		song = album.song_set.all()[0]
		ctx = {'album': album, 'song': song}
	except Album.DoesNotExist:
		raise Http404("The album either has been deleted or never existed")
	return render(resquest, 'web0/detail.html', ctx)

