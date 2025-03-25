from django.shortcuts import render
from main.models import Categories, News

from .forms import Students


def search(request):
    query = request.GET.get('search')
    data = News.objects.filter(title__icontains = query)
    context = {
        'news': data
    }
    return render(request, 'search.html', context)

def studentView(request):
    sf = Students()
    return render(request, 'form.html', {'fm': sf})



def home(request):
    category = Categories.objects.all()
    allNews = News.objects.all().order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category, 
        'allNews': allNews,
        'topNews': topNews
        }
    return render(request, 'index.html', context)

def india(request):
    category = Categories.objects.all()
    
    indiaNews = News.objects.filter(category__title='India News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category, 
        'indiaNews': indiaNews,
        'topNews': topNews
        }
    return render(request, 'categories/india.html', context)


def bolly(request):
    category = Categories.objects.all()
    
    bollyNews = News.objects.filter(category__title='Bollywood News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category, 
        'bollyNews': bollyNews,
        'topNews': topNews
        }
    return render(request, 'categories/bollywood.html', context)


def details(request, id):
    category = Categories.objects.all()
    news = News.objects.get(pk = id)
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'news': news,
        'topNews': topNews
        }
    return render(request, 'details.html', context)
