from django.shortcuts import render, HttpResponse
import matplotlib.pyplot as plt
import scipy.signal as signal
import pyuff


# Create your views here.


def show_windows(request):
    context = {}
    # 根据session中的数据打开当前选中的uff文件
    file_path = request.session.get('file_path')
    uff_file_path = file_path + '/' + request.session.get('file_name')
    uff_file = pyuff.UFF(uff_file_path)
    data = uff_file.read_sets()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    # hann窗
    plt.figure(figsize=(22, 10), dpi=100)
    plt.plot(signal.hann(len(data['data'])))
    """
    图片路径设置规则：在static/imag静态文件中每个文件名称唯一，在每个唯一文件中
    窗函数：hann_window.png
    窗函数加载后的函数：data_hann_window.png
    数据波形图片：data.png
    """
    # 设置图片基础路径
    imag_path = "imag/" + request.session.get("file_name")
    plt.savefig("static/" + imag_path + '/hann_window.png')
    plt.figure(figsize=(22, 10), dpi=100)
    hann_x = data['data'] * signal.hann(len(data['data']), sym=0)
    plt.plot(data['x'], hann_x)
    plt.savefig("static/" + imag_path + '/data_hann_window.png')
    context['hann_window'] = imag_path + '/hann_window.png'
    context['data_hann_window'] = imag_path + '/data_hann_window.png'
    # 三角窗
    plt.figure(figsize=(22, 10), dpi=100)
    plt.plot(signal.triang(len(data['data'])))
    plt.savefig("static/" + imag_path + "/triang_window.png")
    plt.figure(figsize=(22, 10), dpi=100)
    triang_x = data['data'] * signal.triang(len(data['data']), sym=0)
    plt.plot(data['x'], triang_x)
    plt.savefig('static/' + imag_path + '/data_triang_window.png')
    context['triang_window'] = imag_path + '/triang_window.png'
    context['data_triang_window'] = imag_path + '/data_triang_window.png'
    # hamming窗
    plt.figure(figsize=(22, 10), dpi=100)
    plt.plot(signal.hamming(len(data['data'])))
    plt.savefig("static/" + imag_path + "/hamming_window.png")
    plt.figure(figsize=(22, 10), dpi=100)
    hamming_x = data['data'] * signal.hamming(len(data['data']), sym=0)
    plt.plot(data['x'], hamming_x)
    plt.savefig("static/" + imag_path + "/data_hamming_window.png")
    context['hamming_window'] = imag_path + "/hamming_window.png"
    context['data_hamming_window'] = imag_path + "/data_hamming_window.png"
    # 高斯窗
    plt.figure(figsize=(22, 10), dpi=100)
    plt.plot(signal.windows.gaussian(len(data['data']), std=500000))
    plt.savefig("static/" + imag_path + "/gaussian_window.png")
    plt.figure(figsize=(22, 10), dpi=100)
    gaussian_x = data['data'] * signal.gaussian(len(data['data']), std=500000)
    plt.plot(data['x'], gaussian_x)
    plt.savefig("static/" + imag_path + "/data_gaussian_window.png")
    context['gaussian_window'] = imag_path + "/gaussian_window.png"
    context['data_gaussian_window'] = imag_path + "/data_gaussian_window.png"
    # 矩形窗
    plt.figure(figsize=(22, 10), dpi=100)
    plt.plot(signal.boxcar(len(data['data'])))
    plt.savefig("static/" + imag_path + "/boxcar_window.png")
    plt.figure(figsize=(22, 10), dpi=100)
    boxcar_x = data['data'] * signal.boxcar(len(data['data']))
    plt.plot(data['x'], boxcar_x)
    plt.savefig("static/" + imag_path + "/data_boxcar_window.png")
    context['boxcar_window'] = imag_path + "/boxcar_window.png"
    context['data_boxcar_window'] = imag_path + "/data_boxcar_window.png"
    return render(request, 'windows/show_windows.html', context)
