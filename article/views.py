from django.shortcuts import render,redirect
from . models import *
from .forms import *
from django.contrib.auth.decorators import login_required
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

def categorised_article(request,pk):
    if pk == 0:
        articles=Article.objects.all()
        context={
        'articles':articles,
        'category':'all',
        }
    else:
        category=Category.objects.get(pk=pk)
        articles=Article.objects.filter(category=category).all()

        context={
            'articles':articles,
            'category':category,
        }
    return render(request,'article/categoriesd_article.html',context)

# def create_article(request):

#     form = ArticleForm()

#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES) 
#         if form.is_valid():
#             form.save()
#             return redirect('article:index')

#     context = {
#         "form" : form,
#     }

#     return render(request, 'article/article_form.html', context) 

@login_required
def post_article(request): 
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save() 
            return redirect('article:single_article', pk=form.instance.id) 

    context = {
        'form' : form
    } 
    return render(request, 'article/article_form.html', context) 