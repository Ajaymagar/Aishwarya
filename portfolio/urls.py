
from django.contrib import admin
from django.urls import path
from main.views import home , blogs , Iblogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('blogs',blogs,name='blog'),
    path('blogs/<int:pk>',Iblogs,name='Iblogs'),
   

]


