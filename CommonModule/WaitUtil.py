# -*-coding:utf-8 -*-
# @Author : Zhigang

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class WaitUtil(object):
    """封装显示等待方法"""

    def __init__(self,driver):
        "映射定位方式的字典对象"
        self.locationTypeDict={
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "css_selector":By.CSS_SELECTOR,
            "class_name":By.CLASS_NAME,
            "tag_name":By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT
        }

        "初始化driver对象"
        self.driver=driver
        "创建显示等待实例对象"
        self.wait=WebDriverWait(self.driver,10)

    def alertIsPresent(self):
        "判断页面是否出现alert框,并打印alert框消息，当不存在是返回为None"
        try:
            return self.wait.until(EC.alert_is_present()).text
        except Exception as e:
            raise e

    def elementLocatedSelectionStateToBe(self,locationType,locatorExpression, state=True):
        """判断一个元素是否被选中，原方法第一个传入的参数是一个定位器，定位器是一个元组（by, path），
        第二个参数表示期望的元素状态，相等返回True，否则返回False；封装后，传入定位方式和定位表达式，state默认为True
        返回布尔值，未加显示等待"""
        try:
            # 加显示等待的弊端是只有True的时候才会返回，False的时候会引发timeout异常
            # return self.wait.until(EC.element_located_selection_state_to_be\
            #                 ((self.locationTypeDict[locationType.lower()], locatorExpression), state))
            return (EC.element_located_selection_state_to_be\
                             ((self.locationTypeDict[locationType.lower()], locatorExpression), state))(self.driver)
        except Exception as e:
            raise e

    def elementSelectionStateToBe(self,locationType, locatorExpression,state=True):
        "断某个元素是否被选中，原方法第一个参数是一个WebDriver对象，第二个是期望的元素的状态，相等返回True，否则返回False"
        if locationType == "id":
            return EC.element_selection_state_to_be\
                                   (self.driver.find_element_by_id(locatorExpression),state)(self.driver)
        elif locationType == "xpath":
            return EC.element_selection_state_to_be\
                                   (self.driver.find_element_by_xpath(locatorExpression),state)(self.driver)
        else:
            return "未找到定位方式，请确认定位方法是否准确"

    def isTitle(self,title):
        "判断title是否相等,精确匹配，返回布尔值"
        try:
            return EC.title_is(title)(self.driver)
        except Exception as e:
            raise e

    def containsTitle(self,title):
        "判断title是否包含，模糊匹配，返回布尔值"
        try:
            return EC.title_contains(title)(self.driver)
        except Exception as e:
            raise e

    def textToBePresentInElementValue(self,locationType,locatorExpression, text):
        "判断元素的value属性值的文本内容是否出现，返回布尔值"
        try:
            return EC.text_to_be_present_in_element_value\
                               ((self.locationTypeDict[locationType],locatorExpression),text)(self.driver)
        except Exception as e:
            raise e

    def textToBePresentInElement(self,locationType,locatorExpression, text):
        "判断文本内容text是否出现在某个元素中，判断的是元素的text,即text是否是定位元素的字节点，返回布尔值"
        try:
            return EC.text_to_be_present_in_element\
                ((self.locationTypeDict[locationType],locatorExpression), text)(self.driver)
        except Exception as e:
            raise e

    def elementLocatedToBeSelected(self,locationType,locatorExpression):
        "期望某个元素的被选中，如果已被选中返回True,没被选中返回False"
        try:
            return EC.element_located_to_be_selected\
                                   ((self.locationTypeDict[locationType.lower()],locatorExpression))(self.driver)
        except Exception as e:
            raise e

    def elementToBeSelected(self,locationType,locatorExpression):
        "期望某个元素的被选中，函数本身参数为一个WebDriver实例对象,这里统一传入定位方式和定位表达式,返回布尔值"
        if locationType == "xpath":
            return EC.element_to_be_selected(self.driver.find_element_by_xpath(locatorExpression))(self.driver)
        elif locationType == "id":
            return EC.element_to_be_selected(self.driver.find_element_by_id(locatorExpression))(self.driver)
        else:
            return "未找到定位方式，请确认定位方法是否准确"

    def invisibilityOfElementLocated(self,locationType,locatorExpression):
        """ 希望某个元素不可见或者不存在于DOM中，返回布尔值"""
        # 希望某个元素不可见或者不存在于DOM中，满足条件返回True，否则返回定位到的元素对象
        # return self.wait.until(EC.invisibility_of_element_located\
        #     ((self.locationTypeDict[locationType.lower()],locatorExpression)))
        return EC.invisibility_of_element_located\
            ((self.locationTypeDict[locationType.lower()],locatorExpression))(self.driver)

    def presenceOfElementLocated(self,locationType,locatorExpression):
        "显示等待页面元素出现在DOM中，不一定可见，存在则返回该页面元素对象"
        try:
            if self.locationTypeDict[locationType.lower()]:
                element=self.wait.until(EC.presence_of_element_located
                    ((self.locationTypeDict[locationType.lower()],locatorExpression)))
                return element
            else:
                raise TypeError("未找到定位方式，请确认定位方法是否准确")
        except Exception as e:
            raise e

    def frameToBeAvailableAndSwitchToIt(self,locationType,locatorExpression,*args):
        "检查frame是否存在，存在则切换进frame控件中"
        try:
            if self.locationTypeDict[locationType.lower()]:
                self.wait.until(EC.frame_to_be_available_and_switch_to_it
                        ((self.locationTypeDict[locationType.lower()],locatorExpression)))
            else:
                raise TypeError("未找到定位方式，请确认定位方法是否准确")
        except Exception as e:
            raise e

    def visibilityOfElementLocated(self,locationType,locatorExpression,*args):
        "显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象"
        try:
            if self.locationTypeDict[locationType.lower()]:
                element=self.wait.until(EC.visibility_of_element_located
                    ((self.locationTypeDict[locationType.lower()],locatorExpression)))
                return element
            else:
                raise TypeError("未找到定位方式，请确认定位方法是否准确")
        except Exception as e:
            raise e

    def elementToBeClickable(self,locationType,locatorExpression):
        "判断某元素是否可见并且能被点击，条件满足返回该页面元素对象，否则返回False"
        try:
            if self.locationTypeDict[locationType.lower()]:
                element=self.wait.until(EC.element_to_be_clickable
                        ((self.locationTypeDict[locationType.lower()],locatorExpression)))
                return element
            else:
                raise TypeError("未找到定位方式，请确认定位方法是否准确")
        except Exception as e:
            raise e


if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("http://127.0.0.1/test_explicity_wait.html")
    waitUtil = WaitUtil(driver)
    # print (EC.title_is("你喜欢的水果sd")(driver))
    # 验证alertIsPresent()
    # waitUtil.elementToBeClickable("xpath",'// input[ @ onclick = "display_alert()"]').click()
    # print (waitUtil.alertIsPresent())

    # 验证isTitle()和containsTitle()
    # print (waitUtil.isTitle(driver,"你喜欢的水果asd"))
    # print (waitUtil.containsTitle("水果"))

    # 验证textToBePresentInElementValue()
    # print (waitUtil.textToBePresentInElementValue("xpath","//input[@id='text']","今年夏天西瓜相当甜！"))
    # print (waitUtil.textToBePresentInElementValue("xpath",'//option[@id="watermelon"]',"西瓜"))  # 页面未显示，显示未False

    # 验证textToBePresentInElement()
    # print (waitUtil.textToBePresentInElement("xpath",'//p',"请选择你爱吃的水果"))
    # print (waitUtil.textToBePresentInElement("xpath",'//input[@id="check"]',"是否喜欢吃水果？"))
    # print (waitUtil.textToBePresentInElement("xpath",'//option[@id="watermelon"]',"西瓜"))

    # 验证elementLocatedSelectionStateToBe()
    element = Select(driver.find_element_by_xpath('//select[@name="fruit"]'))
    element.select_by_visible_text("西瓜")
    # print (waitUtil.elementLocatedSelectionStateToBe("xpath",'//option[@id="watermelon"]'))
    # print (waitUtil.elementLocatedSelectionStateToBe("xpath",'//option[@id="peach"]'))
    # print(waitUtil.elementLocatedSelectionStateToBe("xpath", '//option[@id="peach"]',state=False))

    # 验证invisibilityOfElementLocated()s
    print(waitUtil.invisibilityOfElementLocated("xpath", '//option[@id="pasdeach"]'))
    print (waitUtil.invisibilityOfElementLocated("xpath",'//option[@id="peach"]'))

    # 验证elementSelectionStateToBe()
    # print (waitUtil.elementSelectionStateToBe("xpath", '//option[@id="peach"]',state=False))
    # print(waitUtil.elementSelectionStateToBe("xpath", '//option[@id="watermelon"]'))
    # print(waitUtil.elementSelectionStateToBe("id", "watermelon"))

    # 验证waitUtil.elementLocatedToBeSelected()
    # print(waitUtil.elementLocatedToBeSelected("xpath", '//option[@id="peach"]'))
    # print (waitUtil.elementLocatedToBeSelected("xpath",'//option[@id="watermelon"]'))

    # 验证elementToBeSelected()
    # print (waitUtil.elementToBeSelected("xpath", '//option[@id="peach"]'))
    # print (waitUtil.elementToBeSelected("id","watermelon"))

    # driver.get("http://mail.126.com")
    # waitUtil=WaitUtil(driver)
    # waitUtil.frameToBeAvailableAndSwitchToIt("xpath",'//iframe[contains(@id,"x-URS-iframe")]')
    # waitUtil.visibilityOfElementLocated("xpath",'//input[@name="email"]').send_keys("yzg18730603667")
    # waitUtil.visibilityOfElementLocated("xpath",'//input[@name="password"]').send_keys("807237157@yzg")
    # waitUtil.elementToBeClickable("xpath",'//a[@id="dologin"]').click()