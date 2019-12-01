from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import registerform

def register(request):
	if request.method == 'POST':
		form = registerform(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account Created for {username}!')
			return redirect('home')
	else:	
		form = registerform()
	return render(request,'../templates/signup.html', {'form': form})
# Create your views here.
