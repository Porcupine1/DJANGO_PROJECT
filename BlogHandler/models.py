from django.db import models


class Aurthor(models.Model):
    name = models.CharField("Author Name", max_length=100)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Ariticle Cnotent")
    pub_date = models.DateTimeField("Publish Date")
    aurthor = models.ForeignKey(Aurthor, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField("Comment")
    pub_date = models.DateTimeField("Publish Date")
    commentor = models.ForeignKey(Aurthor, on_delete=models.CASCADE)
    commented_on = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'comment by {self.commentor}'
