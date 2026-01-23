from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
  def __init__(self,name,age):
    self.name= name
    self.age = age
    
def home(request):
  context={
    'name':'bhavna salve',
    'age':20,
    'skill':['python','django','mysql'],
    'user':User('kumar',30),
    'blog':{
      'title':"Django Template Intro",
      'content': "<b>This is a bold</b>",
      'created_at':datetime(2026,1,23,16,30,20),
      'author' : {
        'name':'Mohit kumar',
      }
    },
    'empty_value':None
  }  
  return render(request,"blog/home.html",context)