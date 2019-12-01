from django.shortcuts import render,redirect
from detail.forms import detailForm
from detail.models import detail
from django.http import *

def viewdetail(request):
	if request.method == "POST":
		form = detailForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				form = detailForm()
				#return redirect()
			except:
				pass
	else:
		form = detailForm()	
	return render(request,"../templates/details.html", {'form':form})
def show(request):
	if request.method == "POST":
		fullname = request.POST.get('fullname')
		details = detail.objects.filter(fullname = fullname)
		return render(request,"../templates/show.html",{'details':details})
	else:
		return render(request,"../templates/search.html",{})


	


