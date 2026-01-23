from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_details(request):
  post = {
    'title':'my second templates post',
    'description':'django is a hevel level web framwwork',
    'author':"Yes",
    'created_at':datetime(2026,1,23,22,47),
    'comment_count':5,
    'tags':['django','python','Web devlopment'],
    'price':100,
    'number':7,
  }
  return render(request,'blog/blog_details.html',{'post':post})