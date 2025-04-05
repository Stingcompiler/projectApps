
from django.urls import path

from . import views

urlpatterns = [
    path('', views.admin_pannel,name='adminP'),
    path('logoutadmin/', views.logoutadmin,name='logoutadmin'),
    path('createAdmin/', views.create_admin,name='createAdmin'),
    path('resetAdmin/', views.reset_admin,name='resetAdmin'),
    path('adminProfile/', views.admin_profile,name='adminProfile'),
    path('del_admin/<int:id>/', views.delete_admin,name='deleteAdmin'),
    
    path('editNews/<int:id>/', views.editNews,name='edit_news'),
    path('deleteNews/<int:id>/', views.deleteNews, name='delete_news'),
    
]