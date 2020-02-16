from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from . import HTV, Movie, camera
from . import music as MUSIC
import random
import cv2
import threading
from .models import Session, MusicSession
from .forms import addSession, addMusicSession

suggestions = [
	'Enjoy these happy vibes with these exuberant hits picked just for you.',
	'Get happy with this pick-me-up playlist full of current feel-good songs picked just for you.',
	'Swipe left to see a surprise ;)',
	'Channelize this energy into productivity. Here are uplifting and energetic music that helps you stay motivated.',
]

# Create your views here.
def index(request):
    return render(request, 'crowdDetection/index.html')

def history(request):
	movies = Session.objects.all()
	music = MusicSession.objects.all()
	return render(request, 'crowdDetection/history.html', {'movies': movies, 'music': music})

def forms(request):
    form = addSession()
    form_music = addMusicSession()
    return render(request, 'crowdDetection/forms.html', {'form': form, 'form_music': form_music})

def movies(request, movie):
    similar_movies = Movie.get_similar(movie)
    viewed_movie = Session.objects.get(movie=movie)
    if viewed_movie.like_factor < 50:
    	return redirect(related_movies, movie)
    return render(request, 'crowdDetection/movies.html', {'movies': similar_movies, 'viewed_movie': viewed_movie, 'message': 'You seem to be engaged with the movie. Here are some picks similar to what you just watched.'})

def related_movies(request, movie):
    emotions = averagedValues()
    similar_movies = Movie.new_movies(emotions)
    viewed_movie = Session.objects.get(movie=movie)
    return render(request, 'crowdDetection/movies_related.html', {'movies': similar_movies, 'viewed_movie': viewed_movie, 'message': 'Looks like you didnt vibe with this one. Here are some worth giving a shot!'})

def music(request, artist):
	music_listened = MusicSession.objects.get(artist=artist)
	prominent = max(music_listened.joy,music_listened.anger,music_listened.surprise,music_listened.sorrow)
	message = suggestions[0]
	if prominent == music_listened.joy:
		prominent = 'joy'
	elif prominent == music_listened.anger:
		prominent = 'anger'
		message = suggestions[3]
	elif prominent == music_listened.sorrow:
		prominent = 'sorrow'
		message = suggestions[1]
	else :
		prominent = 'surprise'
		message = suggestions[2]
	similar_music = MUSIC.get_songs(prominent)
	return render(request, 'crowdDetection/music.html', {'music': similar_music, 'music_listened': music_listened, 'message': message})


def averagedValues():
    sessions = Session.objects.all()
    sorrow = joy = anger = surprise = 0
    for session in sessions:
        sorrow += session.sorrow
        joy += session.joy
        anger += session.anger
        surprise += session.surprise
    length = 1 if len(sessions) == 0 else len(sessions)
    emotions = {'sorrow': round(sorrow / length, 2), 'surprise': round(surprise / length, 2), 'anger': round(anger / length, 2),
                'joy': round(joy / length, 2),}
    return emotions


def closeCam(request):
    if request.method == "POST":
        form = addSession(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            info = camera.stats()
            session.joy = info['joy']
            session.anger = info['anger']
            session.sorrow = info['sorrow']
            session.surprise = info['surprise']
            session.like_factor = info['likeness']
            session.save()
            return redirect(movies, session.movie)
        else:
            form = addSession()
            return redirect(forms)

def addNewMusic(request):
    if request.method == "POST":
        form = addMusicSession(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            info = camera.stats()
            session.joy = info['joy']
            session.anger = info['anger']
            session.sorrow = info['sorrow']
            session.surprise = info['surprise']
            session.like_factor = info['likeness']
            session.save()
            return redirect(music, session.artist)
    else:
        form = addMusicSession()
        return redirect(forms)


def test(request):
    try:
        return StreamingHttpResponse(camera.gen(camera.VideoCamera()),
                                     content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass