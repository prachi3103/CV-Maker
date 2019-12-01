from django import forms
from detail.models import detail

class detailForm(forms.ModelForm):
	"""fullname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	emailid=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	address=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	qualification=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	education=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	interest=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	references=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	Extraskills=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))	
	"""
	class Meta:
		model= detail
		fields= "__all__"

	