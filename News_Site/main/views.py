from django.shortcuts import render
from . import models

# Create your views here.


def home_page(request):
    category = models.Category.objects.all()
    context = {'category': category}
    return render(request, 'main.html', context)


def info(request):
    return render(request, 'info.html')


def articles(request):
    article = models.Article.objects.all()
    context = {'article': article}
    return render(request, 'articles.html', context)


def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    article = models.Article.objects.filter(article_category=category)
    context = {'article': article}
    return render(request, 'exact_category.html', context)


def get_exact_article(request, pk):
    article = models.Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'exact_article.html', context)
