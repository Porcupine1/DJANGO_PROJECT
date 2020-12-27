from django.urls import path
from . import views

app_name = 'BlogHandler'

urlpatterns = [
    path('', views.blog, name='blog'),
]
