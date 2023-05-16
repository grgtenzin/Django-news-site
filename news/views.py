from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def index(request):
    data={
        'catData': Category.objects.all()
    }
    return render(request, 'pages/index.html', data)


def details(request, slug):
    newsData= News.objects.get(slug=slug)
    category= newsData.category.id
    related_news= News.objects.filter(category=category).exclude(id=newsData.id)
    data={
        'newsData': News.objects.get(slug=slug),
        'related_news': related_news,
    }
    return render(request,'pages/details.html', data)


def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['comment']
        send_mail("from: " + email, comment, name,["grgtenzin0@gmail.com"],fail_silently=False,)
        messages.success(request, "your message was sent")
        back = request.META.get('HTTP_REFERER')
        return redirect(back)
    else:
        return render(request, 'pages/contact.html')

def category_news(request,slug):
    Category_data= Category.objects.get(slug=slug)
    data={
        'categoryData': Category_data,
    }
    return render(request, 'pages/category.html', data)

def news(request):
    if request.method=='POST':
        search =request.POST['search']
        find_data= News.objects.filter(title__icontains=search)| News.objects.filter(category__name__icontains=search)
        data={
        'newsD': find_data,
        }
        return render(request, 'pages/news.html', data)

def about(request,slug):
    data={
        'pageData': pages.objects.get(slug =slug)
    }
    return render(request, 'pages/about.html', data)

def money(request):
    return render(request, 'pages/money.html')