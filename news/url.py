from django.urls import path

from . import views

urlpatterns=[
    path('money', views.money,name='money'),
    path('about/<slug:slug>', views.about, name='about'),
    path('news', views.news, name= 'news'),
    path('category_news/<slug:slug>', views.category_news, name='category_news'),
    path('contact', views.contact, name='contact'),
    path('details/<slug>', views.details, name='details'),
    path('', views.index, name='index')
] 