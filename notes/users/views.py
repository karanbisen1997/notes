from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
  if request.method == 'POST':
    username =request.POST['username']
    password =request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      messages.info(request,'LOGIN SUCCESS ')
      return redirect('/')
    else:
      messages.info(request,'INVALID ')
      return redirect('login')
  else:
    return render(request,'users/login.html')

def register(request):
 
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      messages.info(request,'REGISTERED SUCCESS ')
      return redirect('/')
  else:
     form = UserRegisterForm()
  return render(request,'users/register.html',{'form': form})