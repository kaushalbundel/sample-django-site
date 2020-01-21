from django.shortcuts import render
from django.http import HttpResponse
from .models import blog_model
from django.views.generic import (
    ListView,
    DetailView
)

# Create your views here.


def home(request):
    context={
        'posts':blog_model.objects.all()
    }
    return render(request,'blog/home.html',context)

class BlogListView(ListView):
    model=blog_model
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class BlogDetailView(DetailView):
    model=blog_model
    template_name='blog/post_detail.html'
    context_object_name='posts'

def about(request):
    return render(request,'blog/about.html',{'title':about})
