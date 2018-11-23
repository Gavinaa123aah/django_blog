from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.artice_page, name='index'),
]