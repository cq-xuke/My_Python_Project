import xlwings as xw
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
mpl.rcParams['font.sans-serif'] = ['STSong']        #设置全局字体为宋体
data= None
cities = None

def find_city_data(city):           #查找城市内区、县级天气资料
    c_index = cities == city
    return data[c_index,:]


def data_handle(data):              #提取数据，准备作图
    low_t = data[7:43:3]
    high_t = data[8:43:3]
    pre = data[9:43:3]
    data_extract = np.array([low_t, high_t, pre])
    return data_extract


def picture_output(data_extract, city, county):         #作图
    months = ['%s月' % m for m in range(1,13)]
    font = {'family': 'SimHei','color': 'black','weight': 'normal','size': 18}
    #温度折线图
    ymin = int(np.min(np.array(data_extract[0], dtype='float'))//5*5)
    ymax = int(np.max(np.array(data_extract[1], dtype='float'))//5*5+5)
    plt.plot(range(1,13), data_extract[0], 'b-o', label='最低温度')
    plt.plot(range(1,13), data_extract[1], 'r-o', label='最高温度')
    plt.yticks(range(ymin, ymax+1, 5))
    plt.xticks(range(1,13), months)
    plt.grid(linestyle='--')
    plt.legend()
    plt.ylabel("温度(℃)",fontsize = 12)
    plt.title("%s年度气温变化图" % county,fontdict=font)
    for x,y in zip(range(1,13), data_extract[0]):
        plt.text(x-0.3, float(y)+1.2, '%s' % y)
    for x,y in zip(range(1,13), data_extract[1]):
        plt.text(x-0.3, float(y)+1.2, '%s' % y)
    fig = plt.gcf()
    fig.set_size_inches(6.8,4.0)
    plt.savefig(r"C:\Users\cq_xuke\weather_data\%s\%s年度气温变化图.png" % (city, county), dpi=120)
    plt.close()
    #降雨量柱状图
    plt.bar(range(1,13), data_extract[2], label='降雨量')
    ymax = int(np.max(np.array(data_extract[2], dtype='float')) // 25 * 25 + 25)
    plt.xticks(range(1,13), months)
    plt.yticks(range(0, ymax+1, 25))
    plt.legend()
    plt.ylabel("降雨量（mm）",fontsize = 12)
    plt.title("%s年度降雨量变化图" % county, fontdict=font)
    for x,y in zip(range(1,13), np.array(data_extract[2], dtype = float)):
        plt.text(x-0.2, y+2, '%s' % int(y))
    fig = plt.gcf()
    fig.set_size_inches(6.8, 4.0)
    plt.savefig(r"C:\Users\cq_xuke\weather_data\%s\%s年度降雨量变化图.png" % (city, county), dpi=120)
    plt.close()

@xw.sub
def main():
    global data, cities
    wb = xw.Book.caller()
    sht1 = wb.sheets[0]
    sht2 = wb.sheets[1]
    sht2.range("A3").value = "正在作图..."
    data = sht1.range("A2").options(np.array, expand='table').value
    cities = data[:,2]
    city = sht2.range("B1").value
    counties = find_city_data(city)
    if counties.size == 0:
        sht2.range("A3").value = "没有结果，请重新输入城市名"
        return 
    if not os.path.isdir(r'C:\Users\cq_xuke\weather_data\%s' % city):
        os.mkdir(r'C:\Users\cq_xuke\weather_data\%s' % city)
    for county in counties:
        data_extract = data_handle(county)
        location = county[3]
        picture_output(data_extract, city, location)
    sht2.range("A3").value = "作图完成！"