from django.shortcuts import render

from main_page.models import *

def main_page(request):
    context = {
               'posts': Article.objects.all(),
               }
    return render(request, 'main_page/main_page.html', context)

def article(request, article_id):

    post = Article.objects.get(id=article_id)

    context = {
        'title': post.headline,
        'tag': post.publications,
        'text': post.text,
    }
    return render(request, 'main_page/article.html', context)