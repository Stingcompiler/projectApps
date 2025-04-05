from django.db import models

# Create your models here.

class Add_News(models.Model) :
    title = models.CharField(max_length=255,verbose_name="عنوان الخبر")
    shortNews = models.TextField(verbose_name="لمحه عن  الخبر")
    body = models.TextField(verbose_name="محتوى الخبر")
    category = models.CharField(
        max_length=50, 
        choices=[('سياسية', 'سياسية'), ('اقتصادية', 'اقتصادية'), ('ثقافية', 'ثقافية'), ('رياضية', 'رياضية'), ('تقنية', 'تقنية')],
        verbose_name="تصنيف الخبر"
    )
    image_news = models.ImageField(upload_to='pics/',null=True, verbose_name="صورة الخبر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")
    slug = models.SlugField(unique=True, blank=True, null=True)  # حقل الـ Slug

    
    def __str__(self):
        return self.title
    
    
    
from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_key
