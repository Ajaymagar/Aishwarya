from django.shortcuts import render
from .models import Blogs , Project
# Create your views here.

import os

path = os.getcwd()+'/main/cred.json'

import gspread

gc = gspread.service_account(filename=f"{path}")



sh = gc.open_by_key('1fn_DfKa2rmcgLrbIWF8lxrbXn_aQIRQlDiFzBLswb0o')
worksheet = sh.sheet1





def home(request):
   
    projects = Project.objects.all()
    blog  = Blogs.objects.all()
    context = {
        
        'projects':projects,
        'blogs':blog,
                        } 
   
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_data = []
        full_data.extend([name , email ,subject , message])
        worksheet.insert_row(full_data)
        full_data.clear()

    return render(request,'index.html',context)


def blogs(request):
    blog = Blogs.objects.all()
    context = {'blogs':blog}


    return render(request,'blogs.html',context)




def Iblogs(request,pk):
    blog = Blogs.objects.get(pk=pk)
    context = {
        'blog':blog
    }

    return render(request,'blog.html',context)
