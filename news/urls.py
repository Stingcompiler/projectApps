
from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.Add_News,name='news'),
    path('poloticsNews/', views.poloticsNews,name='showPolitics'),
    path('culturalNews/', views.culturalNews,name='cultural'),
    path('economicNews/', views.economicNews,name='economic'),
    path('techNews/', views.techNews,name='techs'),
    path('sportNews/', views.sportsNews,name='sport'),
    #path(' ', views.show_news,name='show_news'),
    path('<slug:slug>/', views.show_news, name='show_news'), 
]