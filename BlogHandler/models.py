from django.db import models
from tinymce.models import HTMLField


class Author(models.Model):
    name = models.CharField("Author Name", max_length=100, null=False)
    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField("Title", max_length=100, null=False)
    pub_date = models.DateTimeField("Publish Date", auto_now_add = True)
    content = HTMLField()
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField("Comment", null=False)
    pub_date = models.DateTimeField("Publish Date", null=False)
    commentor = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    commented_on = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'comment by {self.commentor}'
