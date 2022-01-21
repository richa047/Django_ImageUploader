from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm , PostForm, LoginForm
from django.contrib.auth import authenticate, login, logout 
#from .forms import LoginForm
from.models import Post
from django import forms



from django.contrib import messages

# Home
def home(request):
 posts =Post.objects.all()
 return render(request,'blog/home.html',{'posts':posts})

#About
def about(request):
 return render(request,'blog/about.html')

 #Contact
def contact(request):
 return render(request,'blog/contact.html')

 #Dashboard
def dashboard(request):
  if request.user.is_authenticated:
    posts = Post.objects.all()
    return render(request,'blog/dashboard.html', {'posts':posts})
  else:
    return HttpResponseRedirect('/login/')

def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')

# Signup
def user_signup(request):
   if request.method == "POST":
     form = SignUpForm(request.POST)
     if form.is_valid():
        messages.success(request, 'Congratulations!! you have become an an author')
        form.save()
   else:
        form = SignUpForm()
   return render(request,'blog/signup.html', {'form':form})

#Login
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data= request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user  = authenticate(username=uname, password=upass)
    if user is not None:
        login(request, user)
        messages.success(request,'Logged in Successfully')
        return HttpResponseRedirect('/dashboard/')
  else:     
   form = LoginForm()
   return render(request,'blog/login.html', {'form':form})
 else:
   return HttpResponseRedirect('/dashboard/')
    


 # Add New Post
def add_post(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
        title = form.cleaned_data['title']
        desc = form.cleaned_data['desc']
        pst = Post(title=title, desc=desc)
        pst.save()
        form = PostForm()
         #form.save()
    else:
      form = PostForm()
      return render(request, 'blog/addpost.html', {'form': form})
  else:
   return HttpResponseRedirect('/login/')

    # Update  Post
def update_post(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Post.objects.get(pk=id)
      form = PostForm(request.POST, insatnce=pi)
      if form.is_valid():
        form.save()
    else:
      pi = Post.objects.get(pk=id)
      form = PostForm(instance=pi)
    return render(request, 'blog/updatepost.html')
  else:
   return HttpResponseRedirect('/login/')

    # Delete  Post
def delete_post(request, id):
  if request.user.is_authenticated:
   return HttpResponseRedirect('/dashboard/')
  else:
   return HttpResponseRedirect('/login/')