# -*-coding:utf-8 -*-
# @Author : Zhigang

import os
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendEmail(object):
    """发送邮件类"""

    def __init__(self,sender:str,passwd:str,senderName:str,subject:str,reciver:list,smtpserver="smtp.qq.com"):
        """
        :param sender: 发件人邮箱，字符串类型；本例以qq邮箱举例,可指定默认值
        :param senderName:发件人姓名，字符串类型,可指定默认值；
        :param subject: 邮件主题，字符串类型；
        :param passwd: 发件人邮件密码，字符串类型；本例为qq邮箱授权码,可指定默认值
        :param reciver: 列表类型
        :param smtpserver: 默认值为stmp.qq.com
        """
        self.sender=sender
        self.passwd=passwd
        self.senderName=senderName
        self.subject=subject
        self.reciver=reciver
        self.smtpserver=smtpserver
        self.smtp = smtplib.SMTP()
        self.smtp.connect(self.smtpserver)

    def __emailHeader(self):
        """
        私有方法：邮件标头
        :return: 邮件对象
        """
        message = MIMEMultipart()
        message['From'] = Header(self.senderName, 'utf-8')
        message["To"] = ";".join(self.reciver)
        message['Subject'] = Header(self.subject, 'utf-8')
        return message

    def __connect(self,message):
        """
        私有方法:执行登录、发送和退出动作
        :param message: 邮件对象
        """
        # 打印出和SMTP服务器交互的所有信息，可选择
        # self.smtp.set_debuglevel(1)
        try:
            self.smtp.login(self.sender,self.passwd)
            self.smtp.sendmail(self.sender,self.reciver,message.as_string())
            self.smtp.quit()
        except Exception:
            traceback.print_exc()
            print ("邮件发送失败！")
        else:
            print ("邮件发送成功！")

    def sendText(self,text:str):
        """
        发送纯文本邮件
        :param text: 文本内容
        """
        textPlain = MIMEText(text, 'plain', 'utf-8')
        message=self.__emailHeader()
        message.attach(textPlain)
        self.__connect(message)

    def sendAttachment(self,text:str,*attachPath:str):
        """
        发送任何形式的附件
        :param text: 文本内容
        :param attachPath: 附件路径
        """
        textPlain = MIMEText(text, 'plain', 'utf-8')
        message = self.__emailHeader()
        message.attach(textPlain)
        for attach in attachPath:
            if not os.path.exists(attach):
                print(" {0}附件路径不存在".format(attach))
                return
            attachment = MIMEApplication(open(attach, 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attach))
            message.attach(attachment)
        self.__connect(message)


if __name__=="__main__":
    email=SendEmail("XXXX@qq.com","ymugdjscnghybcjj","刚哥","紧急通知",["XXXX@reapal.com"])
    # email.sendText("见字好:\n  此次邮件通知各位明天开始实施995")
    # email.sendImage("测试方向见图片",r'C:\Users\zhigang\Desktop\test.png')
    # email.sendImage("测试方向见图片", r'\Desktop\自动化测试.png')
    # email.sendAttachment("测试结果见附件",r"C:\Users\zhigang\Desktop\test.png")
    # email.sendAttachment("测试结果见附件", r"C:\Users\zhigang\Desktop\1.html")
    # email.sendAttachment("见字好：\n    今日汇总如下")
    # email.sendAttachment("测试结果见附件", r"C:\Users\zhigang\Desktop\融宝渠道录入收单服务能力.xlsx",
    #                      r"C:\Users\zhigang\Desktop\test.png",r"C:\Users\zhigang\Desktop\1.html")
