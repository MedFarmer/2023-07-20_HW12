from django.shortcuts import render
from django.db.models import Max
from .models import Student

def index(request): # 1. this is to select only certain columns from the database
    selection = Student.objects.values('fname', 'gpa')
    context = {'selection':selection}
    return render(request, 'index.html', context)

def gpa(request): # 2. to select only those whose gpa is greater than 3
    selection = Student.objects.filter(gpa__gt=3)
    context = {'selection':selection}
    return render(request, 'gpa.html', context)


