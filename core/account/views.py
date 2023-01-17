from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
# Create your views here.
def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'شما با موفقیت وارد حسابتان شدید')
        else:
            messages.error(request,'اکانتی یافت نشد دوباره امتحان کنید')
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})

def SignUp(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=User.objects.create_user(email=username,password=password)
        login(request,user)
        print(request.user)
        return redirect('/')
    else:
       return render(request,'register.html',{})