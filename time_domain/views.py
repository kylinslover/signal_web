from django.shortcuts import render
import pyuff
import math
import numpy as np
from scipy import stats

# Create your views here.


def time_domain(request):
    file_path = request.session.get('file_path')
    uff_file_path = file_path + '/' + request.session.get('file_name')
    uff_file = pyuff.UFF(uff_file_path)
    data = uff_file.read_sets()
    # 最大值
    max_value = max(data['data'])
    # 最小值
    min_value = min(data['data'])
    # 平均值
    mean_value = data['data'].mean()
    # 均方根值
    root_mean_value = math.sqrt(sum(x ** 2 for x in data['data']) / len(data['data']))
    # 峰峰值
    pk_value = max(data['data']) - min(data['data'])
    # 绝对平局值
    av_value = abs(data['data']).mean()
    # 峰值因子
    crest_factor_value = pk_value / root_mean_value
    # 波形因子
    shap_factor_value = root_mean_value / av_value
    # 脉冲指标
    impulse_factor_value = pk_value / av_value
    # 裕度指标
    clarance_value = pk_value / pow(abs((sum(np.sqrt([abs(x) for x in data['data']])) / len(data['data']))), 2)
    # 峭度指标
    kur_value = (sum([x ** 4 for x in data['data']]) / len(data['data'])) / pow(root_mean_value, 4)
    # 偏度
    skew_value = stats.skew(data['data'])
    # 方差
    var_value = np.var(data['data'])
    return render(request, "time_domain/time_domain.html", locals())
