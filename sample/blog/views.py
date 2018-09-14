from django.shortcuts import render

# Create your views here.
def index(request):
	"""this returns the view page /home page"""
	return render(request,'blog/index.html')
