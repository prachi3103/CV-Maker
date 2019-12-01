from django import forms
from .models import login

class loginForm(forms.ModelForm):
	class Meta:
		model= login
		fields=[
			'username',
			'password'
		] 
		