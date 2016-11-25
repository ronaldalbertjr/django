from django import forms
from web0.models import Album, Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['file_type', 'song_title', 'song_src']
        widgets = {"user": forms.HiddenInput()}