from django.conf.urls import url
from django.contrib import admin

from .import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^$', views.index, name='index'),
]