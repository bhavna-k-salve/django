from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_list(request):
  blogs = [
    {"title":"Django basic", "is_featured":True ,"author":"john doe"},
    {"title":"Django advanced", "is_featured":False,"author":"bhavna" },
    {"title":"Django framework", "is_featured":True ,"author":"bhavika" }
  ]
  context = {
    "blogs": blogs,
    "today": datetime.now(),
    "html_code":"<h1><b>Welcome to my blog</b></h1>",
  }
  return render (request,'blog/blog_list.html',context)