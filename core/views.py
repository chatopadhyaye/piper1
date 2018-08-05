from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
from .forms import MyUserForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required




# Create your views here.


def signup_form(request):
	if request.method == 'POST':
		f = MyUserForm(request.POST)
		if f.is_valid():
			f.save()
			email = f.cleaned_data.get('email')
			phone = f.cleaned_data.get('phone')
			raw_password = f.cleaned_data.get('password')
			if email is not None:
				email = email.lower()
				user = authenticate(username=email, password=raw_password)
			elif phone is not None:
				user = authenticate(username=phone, password=raw_password)
			login(request, user)
			return redirect("about") # status 201 created
		else:

			return redirect("login") # status 400 bad request
	

	else:
		
		return redirect("login") #status 400 bad request



def login_user(request):


	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			next_url = request.GET.get('next')
			if next_url:
				return HttpResponseRedirect(next_url)
			else:
				return redirect("green")
		else:
			return redirect("login2")



	else:
		f = MyUserForm(request.POST)

		return render(request, 'index.html', {'form': f})




def login2(request):


	if request.method == 'POST':
		email = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			login(request, user)
			next_url = request.GET.get('next')
			if next_url:
				return HttpResponseRedirect(next_url)
			else:
				return redirect("green")
		else:
			return redirect("login2")


	else:
		f = MyUserForm(request.POST)

		return render(request, 'login2.html', {'form': f})







def forgot(request):
	return render(request, 'forgot.html',)


def confirm(request):
	return render(request, 'confirm.html',)


def newpass(request):
	return render(request, 'newpass.html',)