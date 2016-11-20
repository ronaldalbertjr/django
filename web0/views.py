from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.
def index(resquest):
	all_albums = Album.objects.all()
	html = ''
	for album in all_albums:
		url = '/web0/' + str(album.id) + '/'
		html += '<a href="' + url + '">' + album.album_title + '</a></br>' 	
	return HttpResponse(html)


def detail(resquest, album_id):
	return HttpResponse("<h2>Details for Album id: "+str(album_id)+"</h2>")

