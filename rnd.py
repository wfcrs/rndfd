# -*- coding:utf-8 -*-
from random import uniform
import json
import bisect
import pprint
import smtplib
import email
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(content):
    Sender=''                                            # 发件人邮箱账号
    Password = ''                                        # 发件人邮箱密码，如果使用QQ邮箱等，需要使用授权码
    Receiver=''                                          # 收件人邮箱账号，我这边发送给自己
    msg=MIMEText(content,'plain','utf-8')
    msg['From']=formataddr(["",Sender])                  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["",Receiver])                  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="Roll"                                # 邮件的主题

    server=smtplib.SMTP_SSL("smtp.qq.com", 465)          # 发件人邮箱中的SMTP服务器
    server.login(Sender, Password)                       # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(Sender,[Receiver,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit() 
class Rnd():
    def __init__(self):
        with open("./foods.json","r",encoding="utf-8") as json_file:
            self.json_data=json.load(json_file)
        self.Weights_All=0
        for i in self.json_data:
            self.Weights_All+=(self.json_data[i])['weight']
        self.Weights_All=round(self.Weights_All,3)
    def WeightedRandom(self):
        Random_Weight=round(uniform(0,self.Weights_All),2)
        for i in self.json_data:
            Random_Weight-=(self.json_data[i])['weight']
            if(Random_Weight<=0):
                return (self.json_data[i])['name']

Random_Food=Rnd()
content=""
for i in range(0,6):
    content=content+Random_Food.WeightedRandom()+" "
mail(content)
