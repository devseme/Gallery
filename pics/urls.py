from django.conf.urls import url
from django.contrib import admin
from pics import views


urlpatterns=[
    url('admin/', admin.site.urls),
    url(r'^photos/$',views.index,name = 'index')
    ]