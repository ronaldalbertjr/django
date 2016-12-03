from django import forms
from web0.models import Album, Song
from django.contrib.auth.models import User 

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['file_type', 'song_title', 'song_src']
        widgets = {"user": forms.HiddenInput()}

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password']