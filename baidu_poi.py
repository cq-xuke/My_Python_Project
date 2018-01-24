# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:17:48 2018

@author: cq_xuke
"""

import requests
from urllib.parse import urlencode
import json
import math
import xlwings as xw
import numpy as np

region = np.array([31.261, 120.552, 31.386, 120.761])
obj = "学校"
ak = "Your applied ak"
wb = xw.Book()
sht = wb.sheets[0]

def mesh_generator(region):
    x_step = math.ceil((region[2]-region[0])/0.05)+1
    y_step = math.ceil((region[3]-region[1])/0.05)+1
    x = np.linspace(region[0], region[2], x_step)
    y = np.linspace(region[1], region[3], y_step)
    coordinations = []
    for i in range(x_step-1):
        for j in range(y_step-1):
            coordinations.append(tuple([x[i],y[j],x[i+1],y[j+1]]))
    return coordinations


def poi_api(obj, coordination, page_num):
    data = {
            "query": obj,
            "bounds": str(coordination)[1:-1].replace(" ",""),
            "page_size": 20,
            "page_num": page_num,
            "output": "json",
            "ak": ak
            }
    url = "http://api.map.baidu.com/place/v2/search?" + urlencode(data)
    return url


def get_results():
    coordinations = mesh_generator(region)
    row_num = 1
    for coordinate in coordinations:
        for page_num in range(21):
            url = poi_api(obj, coordinate, page_num)
            raw_result = requests.get(url).text
            result = json.loads(raw_result)["results"]
            if len(result) == 0:
                break
            else:
                for rds in result:
                    sht.range((row_num,1)).value = (rds['name'],
                             str(rds['location'])[1:-1], rds['address'])
                    row_num += 1

if __name__ == '__main__':
    get_results()
