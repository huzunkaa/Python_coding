import os
import csv
from django.shortcuts import render,HttpResponse,redirect,reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from pyecharts.charts import Line
from pyecharts import options as opts
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseRedirect
import matplotlib.pyplot as plt

def homepage(response):
    return render(response,'homepages.html')


def analysis(response):
    return render(response, 'analysis.html')


def document(response):
    return render(response,'document.html')

def contact(response):
    return render(response,'contect.html')

def database(response):
    return render(response,'database.html')