from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import record_model
from .models import service_info
from .models import blog_model
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
    content={}
    content['data']=service_info.objects.all()
    return render(request,'index.html',content)

def services(request):
    content={}
    content['data']=service_info.objects.all()
    return render(request,'services.html',content)

def about(request):
    return render(request,'about.html')

def create_record(request):
    if request.method =='POST':
        a = request.POST['cname']
        b = request.POST['cemail']
        c = request.POST['cphone']
        d = request.POST['cservice']
        e = request.POST['cmessage']
        # return HttpResponse(a)
        r1=record_model.objects.create(cname=a,cemail=b,cphone=c, cservice=d,cmessage=e)
        r1.save()
        return redirect('/')
    else:
        return render(request,'index.html')

@user_passes_test(lambda u : u.is_superuser)
@login_required
def insert_service(request):
    return render(request,'insert_service.html')

def insert_service_record(request):
    if request.method == 'POST':
        x= request.POST['sname']
        y= request.POST['sdesc']
        z= request.POST['sdetails']
        s1=service_info.objects.create(sname=x,sdesc=y,sdetails=z)
        s1.save()
        return redirect('services')
    else:
        return render(request,'index.html')    
    
def create_blog_record(request):
    return render(request, 'create_blog.html')

def create_blog(request):
    if request.method == 'POST':
        l= request.POST['btitle'] 
        m= request.POST['bcontent'] 
        n= request.POST['bdate'] 
        b1=blog_model.objects.create(btitle=l,bcontent=m,bdate=n)
        b1.save()
        return redirect('blog')
    else:
        return render(request,'index.html')

def blog(request):
    blog_content={};
    blog_content['data']=blog_model.objects.all()
    return render(request, 'blog.html',blog_content)