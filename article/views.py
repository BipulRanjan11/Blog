from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    all_title=Article.objects.all()
    context={'title':all_title,}
    return render(request,'article/index.html',context)


def single_article(request,pk):
    article=Article.objects.get(pk=pk)
    context={'article_id':article,}
    return render(request,'article/article.html',context)

# without rendering the templates we use context processors inside return for categories now
def categories(request):
    categories=Category.objects.all()
    return {
        'categories':categories
    }