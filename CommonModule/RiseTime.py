# -*-coding:utf-8 -*-
# @Author : Zhigang

import time

def getChineseDate():
    "中文日期"
    return time.strftime("%Y{y}%m{m}%d{d}").format(y="年",m="月",d="日")

def getCurrentDate():
    "数字日期"
    return time.strftime("%Y%m%d")

def getChineseTime():
    "中文时间"
    return time.strftime("%H{H}%M{M}%S{S}").format(H="时",M="分",S="秒")

def getCurrentTime():
    "数字时间"
    return time.strftime("%H:%M:%S")

def getCurrentDateTime():
    "数字日期和时间"
    return time.strftime("%Y-%m-%d %H:%M:%S")


if __name__=="__main__":
    print (getChineseDate())
    print (getCurrentDate())
    print (getChineseTime())
    print (getCurrentTime())
    print (getCurrentDateTime())