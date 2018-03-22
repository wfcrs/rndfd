# -*- coding:utf-8 -*-
from random import uniform
import json
import bisect
import pprint
import smtplib
import email
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(content,Receiver):
    Sender=""
    Password = ""
    msg=MIMEText(content,"plain","utf-8")
    msg["Subject"]="Roll"
    msg["From"]=formataddr(["",Sender])
    server=smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(Sender, Password)
    for i in Receiver:
        msg["To"]=formataddr(["",i])
        server.sendmail(Sender,[i,],msg.as_string())
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
Receiver=[]
for i in range(0,6):
    content=content+Random_Food.WeightedRandom()+" "
mail(content,Receiver)
