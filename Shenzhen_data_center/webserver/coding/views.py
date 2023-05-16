import os
from django.shortcuts import render,HttpResponse,redirect,reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from echarts import Echart, Legend, Line, Tooltip
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseRedirect

def homepage(response):
    return render(response,'homepages.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        # 处理上传文件
        file = request.FILES['file']
        fs = FileSystemStorage('/static/user_file/file_storage/')
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        # 读取文件内容并处理成ECharts所需的数据格式
        data = []
        with open(os.path.join(settings.MEDIA_ROOT, filename), "r") as f:
            for line in f:
                row = line.strip().split("\t")
                data.append([row[0], float(row[1])])
        x_data = [d[0] for d in data]
        y_data = [d[1] for d in data]

        # 构建折线图并渲染到模板上
        chart = Echart('折线图', '示例')
        chart.use(Tooltip())
        chart.use(Legend(['示例']))
        chart.use(Line('示例', y_data, x_axis=x_data))
        chart_data = chart.json
        return render(request, 'chart.html', {'file_url': file_url, 'chart_data': chart_data})
    else:
        return render(request, 'upload.html')