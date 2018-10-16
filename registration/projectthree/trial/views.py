from django.shortcuts import render

# Create your views here.

def try1(request):
	"""my try view """
	return render(request,'trial/try.html')
