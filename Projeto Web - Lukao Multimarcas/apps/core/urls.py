from django.contrib import admin
from django.urls import path
from  apps.core.views import index,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('login/',login, name='login'),
]