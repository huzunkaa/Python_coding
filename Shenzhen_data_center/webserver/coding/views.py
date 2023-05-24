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


def line_chart(request):
    if request.method == 'POST' and request.FILES['txt_file']:
        txt_file = request.FILES['txt_file']
        data = []
        for line in txt_file:
            data.append(line.decode().strip().split())

        # 提取数据并生成折线图
        x_data = []  # x轴数据
        y_data = []  # y轴数据
        for row in data:
            x_data.append(row[0])
            y_data.append(row[1])

        #使用matplotlib作图
        fig,ax = plt.subplots()
        ax.plot(x_data,y_data)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Canvas Plot')
        canvas = fig.canvas


        # 使用pyecharts生成第一个图
        line1 = Line()
        line1.add_xaxis(x_data)
        line1.add_yaxis("折线图", y_data)
        line1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        line1.set_global_opts(title_opts=opts.TitleOpts(title="折线图"))

        # 将折线图呈现在网页上
        return render(request, 'chart.html', {'line': canvas})
    else:
        return render(request, 'chart.html')

def document(response):
    return render(response,'document.html')

def contect(response):
    return render(response,'contect.html')