# -*-coding:utf-8 -*-
# @Author : Zhigang

from Config.ProjectVar import *
import logging.config

# 读取日志的配置文件
logging.config.fileConfig(loggerPath)
# 选择日志格式
logger=logging.getLogger("example01")

def error(message):
    "打印debug级别的信息"
    logger.error(message)

def info(message):
    "打印info级别的信息"
    logger.info(message)

def warning(message):
    "打印warnning级别的信息"
    logger.warning(message)

if __name__=="__main__":
    error("bug ")
    info("自动化测试")
    warning("hello world!")