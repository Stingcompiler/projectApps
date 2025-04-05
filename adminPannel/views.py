from django.shortcuts import render,redirect,get_object_or_404
from news.models import Add_News
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# Create your views here.
@login_required
def admin_pannel(request) :
    if request.method == "POST":
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        category = request.POST.get('category')
        image_news  = request.FILES.get('image')
        shortNews = request.POST.get('shortNews')
        content = request.POST.get('content')
        if Add_News.objects.filter(slug=slug):
           messages.error(request,"عفو رابط موجود ادخل رابطا اخر")
        Add_News.objects.create(title=title,slug=slug,category=category,image_news=image_news,shortNews=shortNews,body=content)
        return redirect('adminP')
    
    newsDetails = Add_News.objects.all()
        
    return render(request,'adminpannel.html' ,{'newsdata':newsDetails})

@login_required
def create_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = True
        is_superuser = request.POST.get('is_superuser') == "on"
        
        if not username or not email or not password:
            messages.error(request, "يرجى ملء جميع الحقول.")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل.")
                
        elif User.objects.filter(email=email).exists():
             messages.error(request, "البريد الإلكتروني موجود بالفعل.")
        
        else:
            try :
                user = User.objects.create(
                    
                    username=username,
                    email=email,
                    password=make_password(password),
                    is_staff = is_staff,
                    is_superuser=is_superuser,
                )
                messages.success(request, "تم إنشاء المسؤول بنجاح.")
                
            except Exception as e:
              messages.error(request, f"حدث خطأ: {e}")
              redirect(request, 'createAdmin')
        
    return render(request,'create_admin.html')
@login_required
def editNews(request,id):
    
            # messages.error(request,"عفو رابط موجود ادخل رابطا اخر")
        newsCheck = Add_News.objects.get(id=id)
        if request.method == "POST":
          newsCheck.title = request.POST.get('title')
          newsCheck.slug = request.POST.get('slug')
          newsCheck.category = request.POST.get('category')
          newsCheck.shortNews = request.POST.get('shortNews')
          newsCheck.content = request.POST.get('content')
          if 'image_news' in request.FILES:
             newsCheck.image_news = request.FILES.get['image']
          newsCheck.save()
          messages.success(request, "تم تحديث الخبر بنجاح!")
          return redirect('adminP')  # Redirect to admin panel

        return render(request, 'edit_news.html', {'news': newsCheck})

@login_required
def deleteNews(request, id):
    try:
        news = Add_News.objects.get(id=id)
        news.delete()
        return redirect('adminP')  # العودة إلى صفحة إدارة الأخبار
    except Add_News.DoesNotExist:
        # معالجة الخطأ إذا لم يتم العثور على الخبر
        return redirect('adminP')

"""
    form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'تم تغيير كلمة المرور بنجاح!')
            return redirect('loginPage')  # Replace with your success URL
        
    else:
        form = PasswordChangeForm(request.user)
"""

@login_required
def admin_profile(request):
  
    admins = User.objects.all()
    adminP ={'admins':admins}
    
    return render(request,'admin_details.html',adminP)


def delete_admin(request, id):
    admin = get_object_or_404(User, id=id)  # Safely get user or return 404
    if admin.is_superuser:  # Prevent deleting superusers
        messages.error(request, "لا يمكنك حذف المسؤول الرئيسي!")
        return redirect('adminProfile')  # Redirect to admin list

    admin.delete()
    messages.success(request, "تم حذف المسؤول بنجاح.")
    return redirect('adminProfile')


User = get_user_model()
@login_required
def reset_admin(request):
    if request.method == "POST":
        old_username = request.POST.get("username")
        new_username = request.POST.get("usernameN")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Get the admin user safely
        admin_user = get_object_or_404(User, username=old_username)

        # Check if the new username already exists
        if new_username and User.objects.filter(username=new_username).exclude(id=admin_user.id).exists():
            messages.error(request, "❌ اسم المستخدم الجديد مستخدم بالفعل.")
            return redirect("resetAdmin")

        # Check if the new email already exists
        if email and User.objects.filter(email=email).exclude(id=admin_user.id).exists():
            messages.error(request, "❌ البريد الإلكتروني مستخدم بالفعل.")
            return redirect("resetAdmin")

        # Update the fields
        if new_username:
            admin_user.username = new_username
        if email:
            admin_user.email = email
        if password:
            try:
                validate_password(password, admin_user)
                admin_user.set_password(password)  # Securely hash the password
                admin_user.save()
                logout(request)  # Logout only if the password was changed
                messages.success(request, "✅ تم تحديث البيانات بنجاح، يرجى تسجيل الدخول مجددًا.")
                return redirect("loginPage")
            except ValidationError as e:
                messages.error(request, " ".join(e.messages))
                return redirect("resetAdmin")

        admin_user.save()
        messages.success(request, "✅ تم تحديث بيانات المسؤول بنجاح.")
        return redirect("loginPage")

    return render(request, "resetAdmin.html")




def logoutadmin(request):
     logout(request)
     return redirect('loginPage')
 