
from django.db import models

# Create your models here.

class profile(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField(default='description text')
	
	def _unicode_ (self):
		
		return self.name
