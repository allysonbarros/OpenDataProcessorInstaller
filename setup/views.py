# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def setup(request):
    title = 'Instalação do OpenDataProcessor'
    return render(request, 'setup.html', locals())