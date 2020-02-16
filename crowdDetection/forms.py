from django import forms
from .models import Session, MusicSession


class addSession(forms.ModelForm):
	class Meta:
		model = Session
		fields = ['movie']


class addMusicSession(forms.ModelForm):
	class Meta:
		model = MusicSession
		fields = ['artist']			
