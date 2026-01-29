from django import models 

class Student(models.Model):
  name = models.CharField()
  age = models.IntegerField()
  
  
student = Student.objects.all()  