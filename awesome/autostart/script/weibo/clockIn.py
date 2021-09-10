#!/usr/bin/env python
# coding=utf-8

"""
    微博超话自动签到
"""

import os
import sys
import time
import json
import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header

ids = [
    {"name": "战斗吧歌姬"  , "id": "100808f6d59f3ee3e0750d8a87d2895d7c5518"} ,

    {"name": "泠鸢yousa"   , "id": "1008081acffb7516358bb316f0052fa9857be8"} ,
    {"name": "hanser"      , "id": "100808bb3bdea1fba9b8b940c3cb788d3f0aae"} ,
    {"name": "小缘"        , "id": "100808a06de9876f35084e6683073a63d9a947"} ,
    {"name": "三无marblue" , "id": "100808db2a58520ac2295a0a7a27903a53e34a"} ,

    {"name": "原神"        , "id": "100808fc439dedbb06ca5fd858848e521b8716"} ,
    {"name": "崩坏3"       , "id": "100808b2be6c70995a36f764be2790db0022f0"} ,
    {"name": "哔哩哔哩"    , "id": "100808502d8075299f18ee3773685119362071"} ,
]

def sendMail(body):
    # 连接邮件服务器
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login('2860307597@qq.com', 'hjrxtkhvhgmbddcc')

    # 邮件内容
    msg = MIMEText(body, 'html', 'utf-8')
    msg['Subject'] = Header('微博超话签到', 'utf-8')
    msg['From'] = Header("RaspberryPi", "utf-8")
    msg['To'] = Header('cyun', 'utf-8')

    # 发送邮件
    server.sendmail("2860307597@qq.com", "cyun@rescld.cn", msg.as_string())

    # 断开连接
    server.quit()

def main():
    string_cookies = ""
    with open(os.path.dirname(__file__) + "/cookies", "r") as f:
        string_cookies = f.read().split('\n')[0]

    cookies = {}
    for i in string_cookies.split('; '):
        line = i.split('=')
        cookies[line[0]] = line[1]

    url = "https://weibo.com/p/aj/general/button"

    params = {
        "ajwvr": 6,
        "api": "http://i.huati.weibo.com/aj/super/checkin",
        "texta": "签到",
        "textb": "已签到",
        "status": 0,
        "location": "page_100808_super_index",
        "timezone": "GMT 0800",
        "lang": "zh-cn",
        "plat": "Linux x86_64",
        "ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "screen": "1920*1080",
        "__rnd": 1618728759077
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "dnt": "1",
    }

    def fun(data, mail):
        if data.get('text', False):
            del data['text']
        if data.get('specialText', False):
            del data['specialText']

        for key in data:
            if type(data[key]) == dict:
                mail = fun(data[key], mail)
            else:
                mail += "<p>{key}: {value}</p>".format(key=key, value=data[key])
        return mail

    mail = "<hr/>"
    for i in ids:
        params["id"] = i["id"]
        headers["referer"] = "https://weibo.com/p/{}/super_index".format(i["id"])
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        try:
            data = json.loads(response.text)
            mail += "<p>{}</p>".format(str(time.asctime(time.localtime(time.time()))))
            mail += "<p>id: {}</p>".format(i['id'])
            mail += "<p>subject: {}</p>".format(i['name'])
            mail = fun(data, mail)
        except Exception as e:
            mail += "<p>{}</p>".format(str(time.asctime(time.localtime(time.time()))))
            mail += "<p>weibo clock error</p>"
            mail += str(e)
            sendMail(mail)
            break
        mail += "<hr/>"
        time.sleep(1)

if __name__ == "__main__":
    main()
