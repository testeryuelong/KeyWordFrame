# -*-coding:utf-8 -*-
# @Author : Zhigang

import os
from CommonModule.RiseTime import *
from Config.ProjectVar import *

def makeChineseDateDir(targetDirPath):
    "以当前日期为目录名在指定路径下创建日期目录"
    if os.path.exists(targetDirPath):
        dirPath=os.path.join(targetDirPath,getChineseDate())
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        return dirPath
    else:
        return "目标路径不存在！"

def makeChineseTimeDir(targetDirPath):
    "以当前时间为目录名在指定路径下创建时间"
    if os.path.exists(targetDirPath):
        dirPath=os.path.join(targetDirPath,getChineseTime())
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        return dirPath
    else:
        return ("目标路径不存在！")

def makeChineseTimePicture(targetDirPath):
    if os.path.exists(targetDirPath):
        picturePath=os.path.join(targetDirPath,getChineseTime()+".png")
        return picturePath
    else:
        return ("目标路径不存在！")

if __name__=="__main__":
    # print (makeChineseDateDir(ScreenshotPath))
    targetDirPath=makeChineseDateDir(screenshotPath)
    # print (makeChineseTimeDir(targetDirPath))
    print (makeChineseTimePicture(targetDirPath))