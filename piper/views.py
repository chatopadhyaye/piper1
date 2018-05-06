from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime




@login_required
def public(request):
	return render(request, 'public.html',)

@login_required
def about(request):
	return render(request, 'about.html',)

@login_required
def edit(request):
	return render(request, 'edit.html',)

@login_required
def privacy(request):
	return render(request, 'privacy.html',)

@login_required
def shared(request):
	return render(request, 'shared.html',)

@login_required
def photos(request):
	return render(request, 'photos.html',)

@login_required	
def videos(request):
	return render(request, 'videos.html',)

@login_required
def album(request):
	return render(request, 'album.html',)

@login_required
def green(request):
	return render(request, 'green.html',)

@login_required
def settings(request):
	return render(request, 'settings.html',)


def user(request):
	return render(request, 'index.html',)

def channel(request):
	return render(request, 'orange_login.html',)
	