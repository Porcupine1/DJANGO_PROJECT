from django.contrib import admin
from .models import Article, Aurthor, Comment


admin.site.register(Article)
admin.site.register(Comment)