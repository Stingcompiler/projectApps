from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        if name and email and subject and message :
            try:
                send_mail(subject, f"From: {name} <{email}>\n\n{message}", settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
                messages.success(request,"تم الارسال شكرا لتواصلك معنا") 
                return redirect('contact') #added return here.

            except BadHeaderError:
                messages.error(request,"invalid")
                return redirect('contact')
        else : 
          messages.error(request,"يرجى ملء جميع الحقول")     
          return redirect('contact')
                
    #news = Add_News.objects.all().order_by('-created_at')
    return render(request ,'contact.html' )


def about(request):
    #news = Add_News.objects.all().order_by('-created_at')
    return render(request ,'about.html' )