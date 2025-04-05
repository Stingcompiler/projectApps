from django.contrib import admin
from .models import Add_News
# Register your models here.
from .models import Visitor

admin.site.register(Visitor)
admin.site.register(Add_News)