from django.contrib import admin
from .models import Student,Course,CommomInfo

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','username']
class AdminCourse(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','cname']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)