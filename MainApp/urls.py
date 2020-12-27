from django.urls import path
from . import views


app_name = 'MainApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.galleryList.as_view(), name='galleryList'),
    path('party/', views.regParty, name='regParty'),
    path('candidate/', views.regCandidate, name='regCandidate'),
    path('party/<pk>/', views.viewPartyDetail.as_view(), name='viewPartyDetail'),
]