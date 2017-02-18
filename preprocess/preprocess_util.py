#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
数据预处理自定义工具函数
"""

import pandas as pd
import time
from math import radians, sin, cos, sqrt, atan2


df_head_with_index = \
    ['iindex', 'lon', 'lat', 'gpstime', 'gpsvelocity', 'northangle', 'vehstatus', 'alarmcode', 'orilon', 'orilat',
    'altitude', 'mile', 'fuel', 'enginetime', 'enginespeed', 'col14', 'col15', 'liquidtemper', 'voltage',
    'insfuel', 'edrspeed', 'oilpressure', 'airpressure', 'torquepercent', 'vehsignalstatus', 'speedfrom',
    'fueltank', 'overspeedalarm', 'col27', 'pedalpos', 'obuvolt', 'enginewatertemper', 'oiltemper',
    'influxtemper', 'dooropen', 'col34', 'col35', 'driverid', 'col37', 'systime', 'soc', 'current', 'volt',
    'col42', 'gears', 'col44', 'col45', 'col46', 'col47', 'col48', 'col49']


def systime2bj(unix_time):
    bj_format = '%Y-%m-%d %H:%M:%S'
    time_array = time.localtime(unix_time/1000)  # 转换为秒级来处理
    dt = time.strftime(bj_format, time_array)
    return dt


def gpstime2bj(gpstime):
    bj_format = '%Y-%m-%d %H:%M:%S'
    gt_date, gt_time = str(gpstime).split('/',2)  # gt means gpstime
    gt_date = gt_date.strip()
    gt_time = gt_time.strip()
    time_array = [int(gt_date[0:4]), int(gt_date[4:6]), int(gt_date[6:8]), int(gt_time[0:2]),
                  int(gt_time[2:4]), int(gt_time[4:6]), 0, 0, 0]
    dt = time.strftime(bj_format, time_array)
    return dt


def distance4gps(lon1, lat1, lon2, lat2):
    """
    reference: http://www.movable-type.co.uk/scripts/latlong.html
    :param lon1:
    :param lat1:
    :param lon2:
    :param lat2:
    :return:
    """
    R = 6371e3  # metres
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi/2.0) * sin(delta_phi/2.0) + \
        cos(phi1) * cos(phi2) * \
        sin(delta_lambda/2.0) * sin(delta_lambda/2.0)
    c = 2.0 * atan2(sqrt(a), sqrt(1.0-a))
    d = R * c
    return d


if __name__ == '__main__':
    unixtime = 1474238421303
    print systime2bj(unixtime)

    gpstime = ' 20160901 / 000124'
    print gpstime2bj(gpstime)

    print distance4gps(116.23, 39.54, 115.48, 38.85)  # 100.3 km
