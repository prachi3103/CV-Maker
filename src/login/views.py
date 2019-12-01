from django.shortcuts import render
from .forms import loginForm
from .models import login

def viewlogin(request):
	form = loginForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = loginForm()

	context = {
		'form': form
	}	
	return render(request,"../templates/login.html", context)




# Create your views here.
