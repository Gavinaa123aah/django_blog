# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . import models


def index(request):
    article = models.Artical.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article': article})
