# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . import models


def index(request):
    articles = models.Artical.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def artice_page(request, article_id):
    article = models.Artical.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
