from django.shortcuts import render,HttpResponse,redirect
from app_final.models import category,articles
from app_final.forms import Registrationform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(req): 
    all_data={
        # 'categories':category.objects.all(),  # Sending using context_processors to all html files
        'articles':articles.objects.filter(status='published',is_trending=True).order_by('-updated_at'),
        'not_trending':articles.objects.filter(status='published',is_trending=False).order_by('-updated_at')
    }
    return render(req,'template1.html',all_data)

def seperate(req,cat):
    key=category.objects.get(category_names=cat)
    context={
        'cat':cat,
        'Articles':articles.objects.filter(category_id=key.id)
    }
    return render(req,'category.html',context)

@login_required(login_url='login page')
def detail_desc(req,slug):
    detail={
        'Articles':articles.objects.get(slug=slug)
    }
    return render(req,'detail_desc.html',detail)

def register(req):
    if req.method=='POST':
        form=Registrationform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login page')
        else:
            return render(req,'register.html',{'form':form})
    form=Registrationform()
    return render(req,'register.html',{'form':form})

def login(req):
    if req.method=='POST':
        form=AuthenticationForm(req,req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(req,user)
                return redirect('home')
        else:
            return render(req,'login.html',{'form':form})

    form=AuthenticationForm()
    return render(req,'login.html',{'form':form})

def logout(req):
    auth.logout(req)
    return redirect('home')




    