from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all() #getting all data from our server
	context = {'posts':posts}
	return render(request,'index.html',context) #passing data to templates

def detail_view(request,pk):
    post = Post.objects.get(id=pk)
    context={'post':post}
    return render(request,'detail.html',context)	