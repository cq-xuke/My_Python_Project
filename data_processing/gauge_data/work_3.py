# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:25:48 2018

@author: cq_xuke
"""

import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt


class TimeError(ValueError):
    def __init__(self):
        self.dolog = "输入的起始时间有误或格式不正确"


class TextError(ValueError):
    def __init__(self):
        self.dolog = "实验号或点号输入格式不正确"


class SampleError(ValueError):
    def __init__(self):
        self.dolog = "重抽样因子不合法"


def sampling(data, weight):  # 抽样：划分矩阵并求划分后的最值
    size = int(data.shape[1])
    quo, rem = divmod(size, weight)
    if rem == 0:
        data_split = np.hsplit(data, size // weight)
    else:
        q_data = data[:, :-rem]
        r_data = data[:, size - rem:]
        data_split = np.hsplit(q_data, q_data.shape[1] // weight)
        data_split.append(r_data)
    sample_list = []
    for array in data_split:
        max_num = max(array[0], key=abs)
        max_num_index = np.where(array[0] == max_num)[0][0]
        max_num_time = array[1][max_num_index]
        sample_list.append([max_num_time, max_num])
    return np.array(sample_list)


def time_search(time_array, time):
    start_index = np.where(time_array >= time[0])[0][0]
    end_index = np.where(time_array <= time[1])[0][-1]
    start_index = int(start_index)
    end_index = int(end_index)
    time_series = time_array[start_index:end_index + 1]
    return start_index + 3, end_index + 3, time_series


@xw.sub
def extract_data(test_code, gauge_point, time, weight):
    wb = xw.Book.caller()
    sht1 = wb.sheets[0]
    code = int(test_code[-1])
    if gauge_point == 2:
        column_num = code * 3 - 1
    elif gauge_point == "f1":
        column_num = code * 3
    else:
        raise TextError
    time_array = sht1.range((3, code * 3 - 2)).options(np.array, expand='vertical').value
    if time_array.max() < time[1] or time[1] < time[0]:
        raise TimeError
    s_index, e_index, time_series = time_search(time_array, time)
    data = sht1.range((s_index, column_num), (e_index, column_num)).options(np.array).value
    if weight < 0 or weight > data.size:
        raise SampleError
    data = np.vstack((data, time_series))
    data_extracted = sampling(data, weight)
    return data_extracted


def draw_picture(data, test_code, gauge_point):
    time_series = data[:, 0]
    point_value = data[:, 1]
    font = {'family': 'SimHei', 'weight': 'normal', 'size': 18}
    plt.plot(time_series, point_value, 'r', linewidth=0.8)
    plt.grid(linestyle='--')
    plt.ylabel('Amplitude(m)')
    plt.xlabel('time(s)')
    title = "The graph of %s's gauge point %s" % (test_code, gauge_point)
    plt.title(title, fontdict=font)
    fig = plt.gcf()
    fig.set_size_inches(6.8, 4.0)
    plt.savefig(r"C:\Users\cq_xuke\work_3\%s.png" % title, dpi=180)
    plt.close()


@xw.sub
def main():
    wb = xw.Book.caller()
    sht2 = wb.sheets[1]
    test_code = sht2.range('B2').value
    gauge_point = sht2.range('B3').options(numbers = int).value
    time = [sht2.range('B4').value, sht2.range('B5').value]
    sht2.range('A7').clear()
    try:
        if not isinstance(time[0], (int, float)):
            raise TimeError
        if not isinstance(time[1], (int, float)):
            raise TimeError
        weight = sht2.range('B6').options(numbers=int).value
        if not isinstance(weight, int):
            raise SampleError
        data = extract_data(test_code, gauge_point, time, weight)
        draw_picture(data, test_code, gauge_point)
        sht2.range('A7').value = '绘图完成！请在"\work_3"目录下查看'
    except TimeError as ex:
        sht2.range('A7').value = ex.dolog
        print(ex.dolog)
    except TextError as ex:
        sht2.range('A7').value = ex.dolog
        print(ex.dolog)
    except SampleError as ex:
        sht2.range('A7').value = ex.dolog
        print(ex.dolog)