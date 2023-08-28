from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.models import User

# Create your views here.


def home_page(request):
    search_bar = forms.SearchForm()
    category = models.Category.objects.all()
    context = {'category': category,
               'form': search_bar}
    return render(request, 'main.html', context)


def info(request):
    return render(request, 'info.html')


def articles(request):
    article = models.Article.objects.all()
    print(article)
    context = {'article': article}
    return render(request, 'articles.html', context)


def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    article = models.Article.objects.filter(article_category=category)
    context = {'article': article}
    return render(request, 'exact_category.html', context)


def get_exact_article(request, pk):
    article = models.Article.objects.get(id=pk)
    print(article)
    article_name = models.Article.objects.get(id=pk)
    comment = models.Comments.objects.filter(comment_article_id=article_name)
    context = {'article': article, 'comment': comment}
    return render(request, 'exact_article.html', context)


def search_product(request):
    if request.method == 'POST':
        get_article = request.POST.get('search_article')
        try:
            exact_aritlce = models.Article.objects.get(product_name__icontains=get_article)
            return redirect(f'articles/{exact_aritlce.id}')
        except:
            return redirect('/')


def add_article_form(request):
    category = models.Category.objects.all()
    context = {'category': category}
    return render(request, 'add_article.html', context)


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def add_comment(request, pk):
    form = forms.CommentForm()
    context = {'id': pk, 'form': form}
    return render(request, 'comment.html', context)


def post_comment(request, pk):
    article_username = models.Article.objects.filter(id=pk)
    username = User.objects.filter(username=request.user.username)
    comment = models.Comments(comment_article_id=article_username.values('pk'),
                              comment_username_id=username.values('pk'),
                              comment_info=request.POST.get('comment_info'))
    comment.save()
    return redirect(f'/articles/{pk}')


def add_article(request):
    form = forms.ArticleForm()
    categories = models.Category.objects.all()
    context = {'form': form, 'category': categories}
    return render(request, 'add_article.html', context)


def post_article(request):
    category = models.Category.objects.filter(category_name=request.POST.get('article_category'))
    article = models.Article(article_name=request.POST.get('article_name'),
                             article_category_id=category.values('pk'),
                             article_info=request.POST.get('article_info'))
    article.save()
    return redirect(f'/')


def delete_article(request, pk):
    delete_article = models.Article.objects.get(id=pk)
    delete_article.delete()
    return redirect(f'/')


def edit_article(request, pk):
    form = forms.ArticleForm()
    categories = models.Category.objects.all()
    context = {'form': form, 'category': categories, 'article_id': pk}
    return render(request, 'edit_article.html', context)


def post_edit_article(request, pk):
    new_category = models.Category.objects.filter(category_name=request.POST.get('article_category'))
    new_article_name = request.POST.get('new_article_name')
    new_article_info = request.POST.get('new_article_info')
    print(models.Article.objects.filter(id=pk))
    if new_article_name == 'Old':
        pass
    else:
        models.Article.objects.filter(id=pk).update(article_name=new_article_name)
    if new_article_info == 'Old':
        pass
    else:
        models.Article.objects.filter(id=pk).update(article_info=new_article_info)
    models.Article.objects.filter(id=pk).update(article_category_id=new_category.values('pk'))

    return redirect('/')




