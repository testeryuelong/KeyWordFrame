# -*-coding:utf-8 -*-
# @Author : Zhigang

import os

# 工程变量路径
projectPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试文件路径
testCaseFile=os.path.join(projectPath,"SourceData","测试文件.xlsx")
testCaseSheetTitle="测试用例"

# 截图目录路径
screenshotPath=os.path.join(projectPath,"Screenshot")

# 日志格式路径
loggerPath=os.path.join(projectPath,"Config","Logger.conf")

# 配置文件路径
configPath=os.path.join(projectPath,"Config","config.ini")

# 测试用例sheet数据
testCaseSheetName = 3
testCaseExecutionOrNot = 4
testCaseExecutedTime = 5
testCaseExecutedResult = 6
# 测试步骤sheet数据
testStepOperation = 2
testStepLocateMethod = 3
testStepLocateExpression = 4
testStepOperateValue = 5
testStepExecutedTime = 6
testStepExecutedResult = 7
testStepErrorInfo = 8
testStepScreenshotPath =9

# 驱动路径，如果已将驱动放在lib/site-package路径下，可以不写
ieDriverPath="d:\\IEDriverServer.exe"
chromeDriverPath="d:\\chromedriver.exe"
firefoxDriverPath="d:\\geckodriver.exe"


if __name__=="__main__":
    print (projectPath)
    print (testCaseFile)
    print (screenshotPath)
    print (loggerPath)