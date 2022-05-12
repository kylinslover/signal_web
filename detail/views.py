from django.shortcuts import render, redirect, HttpResponse
import pyuff
import numpy as np
import matplotlib.pyplot as plt
import os


# Create your views here.


def show_detail(request):
    context = {}
    file_path = request.session.get('file_path')
    uff_file_path = file_path + '/' + request.session.get('file_name')
    uff_file = pyuff.UFF(uff_file_path)
    pre_data_path = file_path + '/' + 'data.txt'
    data = uff_file.read_sets()
    context['data'] = data
    # pre_data = division(data['data'], 8)
    # # 将pre_data 数据储存在data文件中
    # with open(pre_data_path, "wb") as f:
    #     for i in pre_data:
    #         f.writelines(i)
    l = len(data['data']) % 4
    np_data = division(data['data'], 4)
    np.savetxt(pre_data_path, np_data)
    with open(pre_data_path, 'a') as f:
        last_data = data['data'][-l:]
        for i in last_data:
            f.write(str(i))
    with open(pre_data_path, 'r') as f:
        massage = f.read()
    context['massage'] = massage
    # 画出数据波形
    # 设置波形图像路径
    # 图像基础路径
    imag_path = "imag/" + request.session.get("file_name")
    # 查看是否存在文件路径
    if not os.path.exists("static/"+imag_path):
        os.mkdir("static/"+imag_path)
    # 数据波形图像路径
    imag_data_path = imag_path+'/'+'data.png'
    plt.figure(figsize=(22, 10), dpi=100)
    plt.plot(data['x'], data['data'])
    plt.savefig("static/"+imag_data_path)
    context['imag_data_path'] = imag_data_path
    # 数据上传数据库

    return render(request, "detail/detail.html", context)


# 分割data数据
def division(data, n):
    new_data = []
    l = len(data) / n
    for i in range(0, int(l)):
        new_data.append(data[i:i + n])
    np_data = np.array(new_data)
    return np_data


def base(request):
    return render(request, "base.html")


def tablebase(request):
    return render(request, "table.base.html")


def imag_base(request):
    return render(request, "imag.base.html")
