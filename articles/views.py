from django.shortcuts import render
from .models import Article,Archive
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-created_date')
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/article_detail.html', {'article':article})

def archive_list(request):
    archives = Archive.objects.all()
    return render(request, 'articles/archive_list.html',{'archives':archives})

def archive_detail(request,pk):
    arch = Archive.objects.get(pk=pk)
    articles = Article.objects.filter(archive=arch).order_by('-created_date')
    return render(request, 'articles/article_list.html', {'articles':articles})

@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')
