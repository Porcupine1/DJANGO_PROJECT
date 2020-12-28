from django.db import models
from ckeditor.fields import RichTextField


class Author(models.Model):
    name = models.CharField("Author Name", max_length=100, null=False)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField("Title", max_length=100, null=False)
    content = RichTextField(blank=True, null=False)
    pub_date = models.DateTimeField("Publish Date", auto_now_add = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField("Comment", null=False)
    pub_date = models.DateTimeField("Publish Date", null=False)
    commentor = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    commented_on = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'comment by {self.commentor}'
