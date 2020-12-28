from django.urls import reverse
from .models import Article, Author
from django.views.generic import CreateView, DetailView, ListView
from .forms import ArticleForm
from datetime import datetime

class articleCreate(CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        rt = super().form_valid(form)
        article = form.save(commit=False)
        author_name = self.request.POST['author']
        author, created = Author.objects.get_or_create(name=author_name)
        article.author = author
        article.save()
        return rt

    def get_context_data(self, *args, **kwargs):
        context = super(articleCreate, self).get_context_data(*args, **kwargs)
        context['year'] = datetime.timetuple(datetime.now()).tm_year
        return context

    def get_success_url(self):
        return reverse('BlogHandler:articleDetail',args=(self.object.pk,))

class articleDetail(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, *args, **kwargs):
        context = super(articleDetail, self).get_context_data(*args, **kwargs)
        context['year'] = datetime.timetuple(datetime.now()).tm_year
        return context

class articleList(ListView):
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, *args, **kwargs):
        context = super(articleList, self).get_context_data(*args, **kwargs)
        context['year'] = datetime.timetuple(datetime.now()).tm_year
        return context