# -*-coding:utf-8 -*-
# @Author : Zhigang

from selenium import webdriver
from Config.ProjectVar import *
from CommonModule.ObjectMap import *
from CommonModule.ClipboardUtil import *
from CommonModule.KeyBoardUtil import *
from CommonModule.CreateDir import *
from CommonModule.WaitUtil import *
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select

"定义全局driver变量"
driver=None
"全局的等待类实例对象"
waitUtil=None

def open_browser(browserName,*args):
    global driver,waitUtil
    try:
        if browserName.lower() == "ie":
            driver=webdriver.Ie(executable_path=ieDriverPath)
        elif browserName.lower() == "chrome":
            # "创建chrome浏览器的一个options实例对象"
            chrome_options=Options()
            # "添加屏蔽-ignore-certificate-errors提示信息的设置参数项"
            chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
            # "driver对象"
            driver=webdriver.Chrome(executable_path=chromeDriverPath,chrome_options=chrome_options)
            # driver=webdriver.Chrome(executable_path=chromeDriverFilePath)
        else:
            driver=webdriver.Firefox(executable_path=firefoxDriverPath)
        "driver对象创建成功后，创建等待类实例对象"
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url,*args):
    "访问某个网址"
    global  driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*args):
    "关闭浏览器"
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds,*args):
    "强制等待"
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*args):
    "清除输入框默认内容"
    global  driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    "在页面输入框输入数据"
    global  driver
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*args):
    "点击页面元素"
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*args):
    "断言页面源码是否存在某关键字或关键字符串"
    global  driver
    # time.sleep(3)
    try:
        assert assertString in driver.page_source,"{s} not found in page source!".format(s=assertString)
    except AssertionError as e:
        raise AssertionError(e)
    except Exception  as e:
        raise e

def assert_title(titleStr,*args):
    "断言页面标题是否存在给定的关键字符串"
    global  driver
    try:
        assert titleStr in driver.title,"{s} not found in title!".format(s=titleStr)
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def getTitle(*args):
    "获取页面标题"
    global  driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSource(*args):
    "获取页面源码"
    global  driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def switch_to_frame(locationType,frameLocatorExpression,*args):
    "切换进入frame"
    global  driver
    try:
        driver.switch_to.frame(getElement(driver,locationType,frameLocatorExpression))
    except Exception as e:
        raise e

def switch_to_default_content(*args):
    "切出frame,回到默认对话框中"
    global  driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def paste_string(pasteString,*args):
    "模拟ctrl+v操作"
    try:
        Clipboard.setText(pasteString)
        time.sleep(2) # 等待2秒，防止代码执行的太快，而未成功粘贴内容
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

def press_tab_key(*args):
    "模拟tab键"
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

def press_enter_key(*args):
    "模拟enter键"
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    "窗口最大化"
    global  driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def capture_screen(*args):
    "截取屏幕图片"
    global  driver
    # 创建目录，拼接图片保存路径
    targetDirPath = makeChineseDateDir(screenshotPath)
    picNameAndPath = makeChineseTimePicture(targetDirPath)
    # print (picNameAndPath)
    try:
        "截取屏幕图片，并保存为本地文件"
        # driver.get_screenshot_as_file(picNameAndPath.replace("\\",r"\\"))
        driver.get_screenshot_as_file(picNameAndPath)
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def waitPresenceOfElementLocated(locationType,locatorExpression,*args):
    "显示等待页面元素出现在DOM中，不一定可见，存在则返回该页面元素对象"
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,*args):
    "检查frame是否存在，存在则切换进frame控件中"
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*args):
    "显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象"
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except  Exception as e:
        raise e

def selectElementAndString(locationType,locatorExpression,content):
    # 使用xpath定位方式获取select页面元素对象
    if locationType == "xpath":
        selectElement = Select(driver.find_element_by_xpath(locatorExpression))
    elif locationType == "id":
        selectElement = Select(driver.find_element_by_id(locatorExpression))
    # 通过选项的文本选择“B2C网银”选项
    time.sleep(1)
    selectElement.select_by_visible_text(content)

if __name__=="__main__":
    open_browser("chrome")
    visit_url("http://baidu.com")
    capture_screen()
    close_browser()