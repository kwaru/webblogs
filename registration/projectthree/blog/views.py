from django.shortcuts import render

# Create your views here.
def index(request):

	"""this is the home page view"""
	return render(request,'blog/index.html')
