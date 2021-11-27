from django.conf.urls import url
from django.contrib import admin
from pics import views


urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    ]