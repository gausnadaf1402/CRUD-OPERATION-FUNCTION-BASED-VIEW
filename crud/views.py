from django.shortcuts import render,HttpResponseRedirect
from .forms import UserForm
from .models import User

# Create your views here.
def add_student(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
           nm=form.cleaned_data['name']
           em=form.cleaned_data['email']
           pw=form.cleaned_data['password']
           reg=User(name=nm,email=em,password=pw)
           reg.save()
           form=UserForm()
    else:
        form=UserForm()
    stud=User.objects.all()
    return render(request,'enroll/addstudent.html',{'form':form,'stu':stud})

def update_student(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=UserForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=UserForm(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})

def delete_data(request,id):
    pi=User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/add_student')

