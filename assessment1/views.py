from django.shortcuts import render,redirect
from .models import user_master

# Create your views here.
def userhome(request):
    name=request.session.get('username')
    ob=user_master.objects.get(user_name=name)
    return render(request,'userhome.html',{'Username':name,'data':ob})
def adminhome(request):
    name=request.session.get('username')
    obj=user_master.objects.get(user_name=name)
    ob=user_master.objects.filter(roll_name='user')
    return render(request,'adminhome.html',{'Username':name,'data':obj,'user':ob})
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        pwd=request.POST['pwd']
        try:
            ob=user_master.objects.get(user_name=username,password=pwd)
            request.session['username']=ob.user_name
            if ob.roll_name=='user':
                return redirect('userhome')
            elif ob.roll_name=='admin':
                return redirect('adminhome')
        except Exception as e:
            return render(request,'login.html',{'msg':"Invalid user or password " +str(e)})
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