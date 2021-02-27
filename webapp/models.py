from django.db import models

# Create your models here.
class CommomInfo(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=13)
    class Meta:
        abstract=True

class Student(CommomInfo):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.fname

class Course(CommomInfo):
    cname=models.CharField(max_length=20)
    def __str__(self):
        return self.fname