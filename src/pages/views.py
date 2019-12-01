from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,*args, **kwargs):
		print(args, kwargs)
		print(request.user )
		#return HttpResponse ("<h1>Welcome to cvmaker</h1>")
		return render(request,"home.html",{})

def login_view(request,*args, **kwargs):
		print(args, kwargs)
		print(request.user )
		return render(request,"login.html",{})		

def signup_view(request,*args, **kwargs):
		print(args, kwargs)
		print(request.user )
		return render(request,"signup.html",{})		

def details_view(request,*args, **kwargs):
		print(args, kwargs)
		print(request.user )
		#return HttpResponse ("<h1>Welcome to cvmaker</h1>")
		return render(request,"details.html",{})
