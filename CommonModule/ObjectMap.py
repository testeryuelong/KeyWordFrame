# -*-coding:utf-8 -*-
# @Author : Zhigang

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def getElement(driver,locateType,locatorExpression):
    "获取单个页面元素对象"
    try:
        element=WebDriverWait(driver,5).until\
            (lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e

def getElements(driver,locateType,locatorExpression):
    "获取多个页面元素对象，以list返回"
    try:
        elements=WebDriverWait(driver,5).until\
            (lambda x:x.find_elements(by=locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e

def selectElement(driver,locateType,locatorExpression,text):
    "获取下拉框元素对象，通过文本值定位"
    try:
        element=Select(WebDriverWait(driver, 5).until \
            (lambda x: x.find_element(by=locateType, value=locatorExpression)))
        element.select_by_visible_text(text)
    except Exception as e:
        raise e
    # selectElement=Select(driver.find_element_by_xpath('//select[@name="productId"]'))
    # # 通过选项的文本选择“B2C网银”选项
    # selectElement.select_by_visible_text("B2C网银")


if __name__=="__main__":
    driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    driver.get("http://mail.126.com")
    driver.implicitly_wait(10)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]'))
    searchBox=getElement(driver,"xpath",'//input[@name="email"]')
    searchBox.send_keys("123456")
    time.sleep(2)
    driver.quit()