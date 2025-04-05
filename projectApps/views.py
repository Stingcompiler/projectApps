from django.http import HttpResponse
from django.shortcuts import redirect ,render
from news.models import Add_News
from news.models import Visitor
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    total_visitors = Visitor.objects.count()
    
    news = Add_News.objects.all().order_by('-created_at')
    return render(request ,'index.html',{'news':news,'visitor_count':total_visitors})



def serchResults(request):
    query = request.GET.get('search', '').strip()  # حذف الفراغات الإضافية
    results = Add_News.objects.filter(title__icontains=query).order_by('-created_at') if query else Add_News.objects.none()

    all_news = Add_News.objects.all().order_by('-created_at')[:10]  # جلب آخر 10 أخبار كمثال

    # تقسيم نتائج البحث (وليس الأخبار العامة)
    paginator = Paginator(results, 6)  
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'page_obj': page_obj,  # يجب أن يحتوي على النتائج وليس كل الأخبار
        'results': results,  
        'allNews': all_news  # تمرير الأخبار الرائجة للقالب
    }
    

   
    return render(request,'search.html',context)
    
    
    

def my_view(request):
    if 'has_visited' not in request.session:
        # Increment the visitor count
        visitor_count = request.session.get('visitor_count', 0) + 1
        request.session['visitor_count'] = visitor_count
        request.session['has_visited'] = True #Set the flag.
    else:
        visitor_count = request.session.get('visitor_count', 0)
    return HttpResponse(f"Visitor count: {visitor_count}")