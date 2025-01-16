from django.shortcuts import render,redirect
from .models import user_master

# Create your views here.
def login(request):
    return render(request,'login.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        pwd=request.POST['pwd']
        role=request.POST['role']
        ob=user_master.objects.create(user_name=username,password=pwd,roll_name=role)
        ob.save()
        return redirect('login')
    return render(request,'signup.html')