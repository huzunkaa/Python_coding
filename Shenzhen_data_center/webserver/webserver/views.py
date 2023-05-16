# encoding: utf-8
'''
@author:Huzunkai
@name:views.py
@time: 05/10/2023 13:53
@description:
'''
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")