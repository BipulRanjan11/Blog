from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    all_title=Article.objects.all()
    context={'title':all_title,}
    return render(request,'article/index.html',context)