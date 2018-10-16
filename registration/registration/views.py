from django.shortcuts import render

# Create your views here.

def index(request):
	"""this the home page"""


	context={'firstname':'maurice','lastname':'omondi'}
	return render(request,'index.html',context)



def register(request):
	"""this will render registration page"""
	context={'vege1':'cabbage','vege2':'skumawiki','vege3':'kunde'}
	
	return render(request,'register.html',context)
