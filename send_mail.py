#!-*- coding:utf-8 -*-
import smtplib
import string

HOST = "smtp.sina.com" #定义远程主机的地址
SUBJECT="Test email from python" #定义邮件主题
FROM = 'willzhang121@sina.com'
To = 'willzhang121@foxmail.com'
text= "life is short, I use python"

BODY = string.join((
    "From: " + str(FROM),
    "To:" + str(To),
    "Subject:" + str(SUBJECT),
    "",
    text), "\r\n"
)
server = smtplib.SMTP()
server.connect(HOST, "25")
server.starttls()
server.login(FROM, "*********")
server.sendmail(FROM, To, BODY)
server.quit()





























































