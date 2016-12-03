from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from .models import Album, Song
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from web0.forms import SongForm, UserForm

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'web0/index.html'
	context_object_name = 'all_albums'
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = "web0/detail.html"

class  AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class  AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']
	pk_url_kwarg = "album_id"

class AlbumDelete(DeleteView):
	model = Album
	pk_url_kwarg = "album_id"
	success_url = reverse_lazy('web0:index')	

def AddSong(request, album_id):
	form = SongForm()
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'web0/song_form.html', {'form': form, 'album': album})

def AddedSong(request, album_id):
	a = Song()
	a.album = get_object_or_404(Album, pk=album_id)
	a.file_type = request.POST['file_type']
	a.song_title = request.POST['song_title']
	a.song_src = request.FILES['song_src']
	if not a.album.song_set.all():
		favorited = False
	else:
		for song in a.album.song_set.all():
			if song.is_favorite:
				favorited = True
			else:
				favorited = False
	if not favorited:
		a.is_favorite = True
	a.save()
	return render(request, 'web0/song_added.html')

class UserFormView(generic.View):
	form_class = UserForm
	template_name = 'web0/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):	
		form = self.form_class(request.POST)	
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns user object if credentials are correct
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('web0:index')
		else:
			return render(request, self.template_name, {'form': form})


		

