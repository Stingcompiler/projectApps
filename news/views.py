from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Add_News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Add_News  # Replace with your actual model
# Create your views here.

def addNews(request):
    if request.method == "POST" :
        pass




def show_news(request, slug):
    moreNews = Add_News.objects.all().order_by('-created_at')
    recievNews = get_object_or_404(Add_News, slug=slug)

    paginator = Paginator(moreNews, 6)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'news': recievNews,
        'allNews':moreNews
        # Include recievNews directly
    }

    return render(request, 'show_news.html', context)



def poloticsNews(request) :
    moreNews = Add_News.objects.all().order_by('-created_at')
    

    paginator = Paginator(moreNews, 6)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
      
        'allNews':moreNews
        # Include recievNews directly
    }
  
    return render(request,'politics.html',context)


def culturalNews(request):
    moreNews = Add_News.objects.all().order_by('-created_at')
    

    paginator = Paginator(moreNews, 6)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
      
        'allNews':moreNews
        # Include recievNews directly
    }

    return render(request, 'cultural.html', context)





def economicNews(request) :
    moreNews = Add_News.objects.all().order_by('-created_at')
    

    paginator = Paginator(moreNews, 6)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
      
        'allNews':moreNews
        # Include recievNews directly
    }
  
    return render(request,'economic.html',context)


def sportsNews(request) :
    moreNews = Add_News.objects.all().order_by('-created_at')
    

    paginator = Paginator(moreNews, 6)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
      
        'allNews':moreNews
        # Include recievNews directly
    }
    return render(request,'sports.html',context)


def techNews(request) :
    moreNews = Add_News.objects.all().order_by('-created_at')
    

    paginator = Paginator(moreNews, 6)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
      
        'allNews':moreNews
        # Include recievNews directly
    }
    return render(request,'technologies.html',context)

