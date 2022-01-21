from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
       #one way to save data in db
        #if fm.is_valid():
        # fm.save()
      # 2nd way to save data in db.

      #To access data & save data in db.
     if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg = User(name=nm, email=em, password=pw) 
      reg.save()
      # Clear the form after  submitted to the db
      fm = StudentRegistration()
             
    else:
      fm =StudentRegistration()
      #to call all the db data on the frontend page
    stud = User.objects.all()

    return render(request, 'enrollapp/addandshow.html',{'form':fm,'stu':stud})

    # This Function will Delete
def delete_data(request, id):
  if request.method == 'POST':
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

     # This Function will update and edit
def update_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(request.POST, instance = pi)
     if fm.is_valid():
        fm.save()
     else:
       pi = User.objects.get(pk= id)
       fm = StudentRegistration(instance=pi)
       console.log(fm)
     return render(request,'enrollapp/updatestudent.html' , {'form':fm})

