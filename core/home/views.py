from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples=[
        {'name':'Abhijeet gupta' , 'age':23},
        {'name':'rohan sharma' , 'age':24},
        {'name':'vicky kaushal' , 'age':28},
        {'name':'deepanshu shar' , 'age':  7},
        {'name':'sandeep' , 'age':31}

    ]

    vegetables = ['Pumpkin', 'Tomato', 'Potatoe']

    # for people in peoples:
    #     print(peoples)

    return render(request,'home/index.html', context = { 'peoples' : peoples , 'vegetables' : vegetables } )

def about(request):
    title = 'About'
    return render(request,'home/about.html',{'title':title})

def contact(request):
    title = 'Contact'
    return render(request,'home/contact.html',{'title' : title})