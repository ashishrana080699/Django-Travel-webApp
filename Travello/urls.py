from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('index.html', views.Home, name='home'),
    path('about.html',views.About,name='about'),
    path('news.html', views.News, name='news'),
]
