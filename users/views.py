from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from projectApps import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        checkUser = authenticate(username=username, password=password)
        if checkUser is not None:
            # Authentication successful, log the user in
            login(request, checkUser)
            return redirect('adminP')
        else:
            # Authentication failed, you might want to add an error message
            # For example:
            # error_message = "Invalid username or password"
            # return render(request, 'loginPage.html', {'error': error_message})
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة') #
            return render(request, 'loginPage.html')

    return render(request, 'loginPage.html')

User = get_user_model()

def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        try:
            user = User.objects.get(email=email)
            
            # Generate token & UID
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.id))

            reset_url = f"https://musab.stingdev.uk/users/confirmPassword/{uid}/{token}/"

            # Email details
            subject = 'إعادة تعيين كلمة المرور'
            message = f"يرجى النقر على الرابط التالي لإعادة تعيين كلمة المرور:\n{reset_url}"
            html_message = f"""
                <p>يرجى النقر على الرابط التالي لإعادة تعيين كلمة المرور:</p>
                <a href="{reset_url}">إعادة تعيين كلمة المرور</a>
            """

            email_message = EmailMultiAlternatives(
                subject, message, settings.EMAIL_HOST_USER, [email]
            )
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()

            messages.success(request, "تم إرسال رابط إعادة تعيين كلمة المرور إلى بريدك الإلكتروني.")
            return redirect('resetPass')
        
        except User.DoesNotExist:
            messages.error(request, "البريد الإلكتروني غير مسجل.")
        
        except Exception as e:
            messages.error(request, "حدث خطأ أثناء إرسال البريد الإلكتروني. حاول مرة أخرى.")

        return redirect('resetPass')

    return render(request, 'reset_password.html')




User = get_user_model()

def confirm_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, id=uid)

        if not default_token_generator.check_token(user, token):
            messages.error(request, "رابط إعادة تعيين كلمة المرور غير صالح أو انتهت صلاحيته.")
            return redirect('resetPass')

        if request.method == "POST":
            password = request.POST.get("new_password")

            if not password:
                messages.error(request, "يرجى إدخال كلمة مرور جديدة.")
                return render(request, 'confirmPassword.html', {'uidb64': uidb64, 'token': token})

            try:
                validate_password(password, user)
            except ValidationError as e:
                messages.error(request, " ".join(e.messages))
                return render(request, 'confirmPassword.html', {'uidb64': uidb64, 'token': token})

            user.set_password(password)
            user.save()
            messages.success(request, "تم تغيير كلمة المرور بنجاح.")
            return redirect('loginPage')

        return render(request, 'confirmPassword.html', {'uidb64': uidb64, 'token': token})

    except (TypeError, ValueError, OverflowError):
        messages.error(request, "الرابط غير صالح.")
        return redirect('resetPass')