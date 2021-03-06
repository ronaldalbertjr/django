from django.conf.urls import url
from . import views

app_name = "web0"
urlpatterns = [
	# /web0/
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    #/web0/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /web0/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /web0/<album_id>/addsong
    url(r'^(?P<album_id>[0-9]+)/addsong/$', views.AddSong, name='song-add'),

    # /web0/<album_id>/addedsong
    url(r'^(?P<album_id>[0-9]+)/addedsong/$', views.AddedSong, name='song-added'),

    # /web0/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/web0/album/<album_id>/
    url(r'album/(?P<album_id>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/web0/album/<album_id>/delete
    url(r'album/(?P<album_id>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]