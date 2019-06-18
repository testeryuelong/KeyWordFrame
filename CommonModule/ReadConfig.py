# -*-coding:utf-8 -*-
# @Author : Zhigang

from configparser import ConfigParser
from Config.ProjectVar import *

class ReadConfig(object):
    """封装常用的读取配置文件方法"""

    def __init__(self,configPath):
        self.config=ConfigParser()
        self.config.read(configPath)

    def getAllSections(self):
        "返回配置文件中所有的section"
        return self.config.sections()

    def getSection(self,sectionName):
        "返回配置文件中指定section下的所有内容，如果存在则以字典形式返回{option:value}，不存在返回None"
        if self.hasSection(sectionName):
            return dict(self.config.items(sectionName))
        else:
            return None

    def getValue(self,sectionName,optionName):
        "返回配置文件中指定section下的指定option的值,否则返回None"
        if self.hasOption(sectionName,optionName):
            return self.config.get(sectionName,optionName)
        else:
            return None

    def hasSection(self,sectionName):
        "判断配置文件中是否存在section,返回布尔值"
        return self.config.has_section(sectionName)

    def hasOption(self,sectionName,optionName):
        "判断配置文件中在section下是否存在指定option,返回布尔值"
        return self.config.has_option(sectionName,optionName)


if __name__=="__main__":
    # cf=ConfigParser()
    # cf.read(configPath)
    # print (cf.sections())
    # print (cf.items("百度"))
    # print (cf.options("百度"))
    # print (cf.get("百度","inputbox"))
    rd=ReadConfig(configPath)
    print (rd.getAllSections())
    print (rd.getSection("百度"))
    print (rd.getSection("asd"))
    print (rd.hasOption("百度","inputbox"))
    print(rd.hasOption("百度", "iasnputbox"))
    print (rd.getValue("百度","inputbox"))
    print(rd.getValue("百度", "iasnputbox"))