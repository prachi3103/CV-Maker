from django.db import models

class login(models.Model):

	email = models.EmailField(max_length=120, default=True)
	username = models.CharField(max_length=120, blank=False)
	password = models.CharField(max_length=32, blank=False)
	confirmpassword = models.CharField(max_length=32, default=True)

	def __str__(self):
		return self.username

	# Create your models here.
