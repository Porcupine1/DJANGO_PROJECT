from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Article, Aurthor, Comment
from datetime import datetime


def blog(request):
    articles = Article.objects.all()
    context = {
        'date': datetime.timetuple(datetime.now()).tm_year,
        'articles': articles
    }
    if request.method == 'POST':
        aurthor = Aurthor(name=request.POST['aurthor_name'])
        article = Article(title=request.POST['article_title'],
                          content=request.POST['article_content'],
                          pub_date=str(datetime.now().date()),
                          aurthor=aurthor)
        aurthor.save()
        article.save()
        return redirect(reverse('BlogHandler:blog', args=()))
    return render(request, 'BlogHandler/blog.html', context)
