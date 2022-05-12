import datetime

from django.shortcuts import render, redirect
from .forms import UffForm
from .models import UffFile
# Create your views here.
import os


def handle_upload_file(f):
    """
    对上传文件的预先处理
    获取文件内容并保存到本地服务器中
    且获取服务器文件路径
    :param f:
    :return:
    """
    file_path = 'upload/'+f.name
    # 判断路径是否存在保持文件名称的唯一性
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    else:
        pass
    # 如果存在该路径则覆盖原文件
    with open(file_path + '/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return file_path


def upload(request):
    """
    获取文件的内容并保存到session中
    并在数据库中进行存储
    :param request:
    :return:
    """
    context = {}
    if request.POST:
        form = UffForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_upload_file(request.FILES["file_field"])
            # 将该文件置于session中，设置为当前分析文件
            request.session['file_path'] = file_path
            request.session['file_name'] = request.FILES["file_field"].name
            # 判断数据库中是否含有该记录，若含有该记录则更新，否则添加
            date = datetime.datetime.now()
            file_exit = UffFile.objects.filter(file_path=file_path).exists()
            if not file_exit:
                this_file = UffFile.objects.create(file_path=file_path, file_name=request.FILES["file_field"].name,
                                                   upload_time=date)
            else:
                UffFile.objects.filter(file_path=file_path).update(file_name=request.FILES["file_field"].name,
                                                                   upload_time=date)
        return redirect("detail:show_detail")
    else:
        form = UffForm()
    context['form'] = form
    return render(request, 'upload/upload.html', context)

# def save_database(file_path, file_name):
