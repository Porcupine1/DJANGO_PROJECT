from django.urls import path
from . import views

app_name = 'BlogHandler'

urlpatterns = [
    #path('', views.articleList.as_view(), name='articleList'),
    path('', views.articleCreate.as_view(), name='articleCreate'),
    path('<pk>', views.articleDetail.as_view(), name='articleDetail')
]
