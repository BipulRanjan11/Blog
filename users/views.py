from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
# for take data and modify we will
def register(request):

    if request.method=='POST':
        form=NewRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('article:index')
    else:
        form=NewRegisterForm()
    context={
        'form':form
    }
    return render(request,'users/register.html',context)


def profile(request):
    return render(request,'users/profile.html')
