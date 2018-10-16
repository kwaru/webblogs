from django.db import models

# Create your models here.


class registration_data(models.Model):
	"""this is for our registration page"""
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	email=models.CharField(max_length=100)

	
