# -*-coding:utf-8 -*-
# @Author : Zhigang

from CommonModule.ParseExcel import *
from Config.ProjectVar import *
import traceback
from KeywordFunction.PageAction import *
from CommonModule.Log import *

def run(testCaseFile,testCaseSheetTitle):
    "主程序，参数为测试文件和测试文件的测试用例名字"
    excelObj=ParseExcel(testCaseFile)
    excelObj.setExcelOprateSheet(testCaseSheetTitle)
    for idx in range(2,excelObj.getMaxRow()+1):
        if excelObj.getTargetCellValue(idx,testCaseExecutionOrNot).lower() == "y":
            # 清空内容
            excelObj.clearValue(testCaseSheetTitle,idx,testCaseExecutedTime)
            excelObj.clearValue(testCaseSheetTitle,idx,testCaseExecutedResult)
            testStepSheet=excelObj.getTargetCellValue(idx,testCaseSheetName)
            excelObj.clearSheetValue(testStepSheet)
            # 拼接函数并执行
            successStep=0 # 通过执行步骤的总数来决定测试用例最后的执行结果
            for id in range(2,excelObj.getMaxRow()+1):
                stepRow=excelObj.getTargetRowObj(id)
                operation=stepRow[testStepOperation-1].value
                locateMethod=stepRow[testStepLocateMethod-1].value
                locateExpression=stepRow[testStepLocateExpression-1].value
                operateValue=stepRow[testStepOperateValue-1].value
                # print (operation,locateMethod,locateExpression,operateValue)
                if operation is not None and locateMethod is None \
                    and locateExpression is None and operateValue is not None:
                    command="%s('%s')" % (operation,operateValue)
                elif operation is not None and locateMethod is not None \
                    and locateExpression is not None and operateValue is not None:
                    command="%s('%s','%s','%s')" % (operation,locateMethod,locateExpression,operateValue)
                elif operation is not None and locateMethod is not None \
                    and locateExpression is not None and operateValue is None:
                    command="%s('%s','%s')" % (operation,locateMethod,locateExpression)
                elif operation is not None and locateMethod is None \
                    and locateExpression is None and operateValue is None:
                    command = "%s()" % (operation)
                # print (command)
                try:
                    eval(command)
                except Exception:
                    error("测试步骤 %s ：执行失败" % command)
                    excelObj.writeCellStrValue(id,testStepExecutedResult,content="fail", style="red")
                    excelObj.writeCellStrValue(id,testStepErrorInfo, content=traceback.format_exc(), style="red")
                    excelObj.writeCellStrValue(id,testStepScreenshotPath, content=capture_screen(), style="red")
                else:
                    successStep+=1
                    info("测试步骤 %s ：执行成功" % command)
                    excelObj.writeCellStrValue(id,testStepExecutedResult,content="pass",style="green")
                finally:
                    excelObj.writeCellStrValue(id,testStepExecutedTime,content=getCurrentDateTime())
            # 在测试用例中写入最后的运行结果
            if successStep == excelObj.getMaxRow()-1:
                info("测试用例 %s:测试通过" % testStepSheet)
                excelObj.setExcelOprateSheet(testCaseSheetTitle)
                excelObj.writeCellStrValue(idx,testCaseExecutedResult,content="pass",style="green")
            else:
                error("测试用例 %s:测试失败" % testStepSheet)
                excelObj.setExcelOprateSheet(testCaseSheetTitle)
                excelObj.writeCellStrValue(idx,testCaseExecutedResult,content="fail",style="red")
            excelObj.writeCellStrValue(idx,testCaseExecutedTime,content=getCurrentDateTime())
        else:
            testStepSheet=excelObj.getTargetCellValue(idx,testCaseSheetName)
            info("测试用例 %s : 忽略，不执行" % testStepSheet)


if __name__=="__main__":
    run(testCaseFile, testCaseSheetTitle)