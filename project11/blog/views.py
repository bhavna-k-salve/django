from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'base.html')

def blog(request):
  student_list =[
    {"name":"bhavna","class":"10th"},
    {"name":"bhavika","class":"9th"},
    {"name":"bhanu","class":"8th"},
    {"name":"bhaskar","class":"7th"},
  ]
  return render(request,'blog.html',{'students':student_list})