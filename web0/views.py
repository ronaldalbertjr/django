from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Album
# Create your views here.
def index(resquest):
	all_albums = Album.objects.all()
	ctx = {'all_albums': all_albums}
	return render(resquest, 'web0/index.html', ctx)


def detail(resquest, album_id):
	album = get_object_or_404(Album,id=album_id)
	song = album.song_set.get(is_favorite=True)
	ctx = {'album': album, 'song': song}
	return render(resquest, 'web0/detail.html', ctx)

def favorite(resquest, album_id):
	album = get_object_or_404(Album, id=album_id)
	try:
		selected_song = album.song_set.get(pk=resquest.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(resquest, 'web0/detail.html' ,{'album': album, 'error_message': 'You did not select a valid song',})
	else:
		for song in album.song_set.all():
			song.is_favorite = False
			song.save() 
		selected_song.is_favorite = True
		selected_song.save()
		ctx = {'album':album, 'song': selected_song}
		return render(resquest, 'web0/detail.html', ctx)
