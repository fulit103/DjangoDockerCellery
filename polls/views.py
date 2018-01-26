# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import random


from .tasks import add

def index(request):
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    add.delay( x, y )
    print "index %s + %s " % (x, y )
    return HttpResponse("Hello, world. You're at the polls index.")