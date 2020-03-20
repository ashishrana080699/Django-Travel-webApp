from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('about.html',views.about,name='about'),
    path('contact.html', views.contact_page, name='contact'),
    path('news.html', views.news, name='news'),
    path('contact_submit', views.contact_submit, name='contact_submit'),
]
