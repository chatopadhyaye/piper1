from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime




def public(request):
	return render(request, 'public.html',)


def about(request):
	return render(request, 'about.html',)


def edit(request):
	return render(request, 'edit.html',)


def privacy(request):
	return render(request, 'privacy.html',)


def shared(request):
	return render(request, 'shared.html',)


def photos(request):
	return render(request, 'photos.html',)


def videos(request):
	return render(request, 'videos.html',)


def album(request):
	return render(request, 'album.html',)


def green(request):
	return render(request, 'green.html',)


def settings(request):
	return render(request, 'settings.html',)


def user(request):
		return render(request, 'index.html',)


def channel(request):
	return render(request, 'orange_login.html',)
	