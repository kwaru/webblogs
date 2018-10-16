from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list_view(request):

	posts=Post.published.all()
	return render(request,'blog/list.html',{'posts':posts})

def post_detail_view(request,year,month,day,post):

	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    	return render(request,'blog/detail.html',{'post':post})



def new_post(request):
	"""new request page controller"""

	return render(request,'blog/new_post')
