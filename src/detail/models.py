from django.db import models

class detail(models.Model):# Create your models here.

	fullname=models.CharField(max_length=200, blank=False)
	contact=models.CharField(max_length=10)
	emailid=models.EmailField(default=None)
	address=models.CharField(max_length=400)
	careerobj=models.CharField(max_length=800,default=None)
	qualification=models.CharField(max_length=800)
	education=models.CharField(max_length=800)
	interest=models.CharField(max_length=800)
	references=models.CharField(max_length=800)
	Extraskills=models.CharField(max_length=800,blank=True)
	
	class Meta:
		db_table = "detail"



