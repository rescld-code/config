#!/usr/bin/env python
# coding=utf-8

"""
    B站直播间自动打卡
    打卡间隔5秒
"""

import os
import sys
import time
import json
import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header

# 默认发送的消息
send_string = "(=・ω・=)"

"""
    自动打卡参数
    id:     用户名，给自己看的
    uid:    up主的 uid，必填
    roomid: 直播间 id，必填
    msg:    (string, boolean)
            - string 表示需要发送的消息
            - boolean是否发送自定义消息，False发送默认消息
"""
live_room = [
        { "id": "泠鸢yousa"          , "uid": 282994     , "roomid": 47377     } ,
        { "id": "hanser"             , "uid": 11073      , "roomid": 48743     } ,
        { "id": "三无Marblue"        , "uid": 284120     , "roomid": 544622    } ,

        { "id": "战斗吧歌姬官方账号" , "uid": 364225566  , "roomid": 14578426    , "msg": ("战斗吧歌姬，时刻回应爱！" , False) } ,
        { "id": "小豆芽安雪璃"       , "uid": 323153     , "roomid": 609304    } ,
        { "id": "❀Sakulaˇ小舞"       , "uid": 264161     , "roomid": 837039    } ,
        { "id": "鱼一YY"             , "uid": 1308967115 , "roomid": 23029299  } ,

        { "id": "琉绮Ruki"           , "uid": 420249427  , "roomid": 21403609  } ,
        { "id": "七海Nana7mi"        , "uid": 434334701  , "roomid": 21452505  } ,

        { "id": "咩栗"               , "uid": 745493     , "roomid": 8792912   } ,
        { "id": "呜米"               , "uid": 617459493  , "roomid": 22384516  } ,

        { "id": "田汐汐_Official"    , "uid": 473764233  , "roomid": 21627536  } ,
        { "id": "小虾鱼Official"     , "uid": 358695457  , "roomid": 13576775  } ,

        { "id": "千春_Chiharu"       , "uid": 558070433  , "roomid": 22389319  } ,
        { "id": "诗小雅Official"     , "uid": 36576761   , "roomid": 6129586   } ,
]


data = {
    "color": 5566168,
    "fontsize": 25,
    "bubble": 0,
    "csrf_token": "86ce07f41e5886f416b2aec505a75897",
    "csrf": "86ce07f41e5886f416b2aec505a75897"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

def sendMail(body):
    # 连接邮件服务器
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login('2860307597@qq.com', 'hjrxtkhvhgmbddcc')

    # 邮件内容
    msg = MIMEText(body, 'html', 'utf-8')
    msg['Subject'] = Header('Bilibili直播间打卡', 'utf-8')
    msg['From'] = Header("RaspberryPi", "utf-8")
    msg['To'] = Header('cyun', 'utf-8')

    # 发送邮件
    server.sendmail("2860307597@qq.com", "cyun@rescld.cn", msg.as_string())

    # 断开连接
    server.quit()

def sendMsg(msg, cookies):
    url = "https://api.live.bilibili.com/msg/send"

    for i in live_room:
        # 获取指定的发送内容
        try:
            if i["msg"][1]:
                data["msg"] = i["msg"][0]
            else:
                data["msg"] = msg
        except KeyError:
            data["msg"] = msg

        # 设置请求参数
        data["rnd"] = i["uid"]
        data["roomid"] = i["roomid"]

        #  发送请求
        response = requests.post(url, headers=headers, cookies=cookies,data=data)

        # 获取响应
        result = json.loads(response.content.decode())

        # 发送失败，记录文件
        body = "<hr/>"
        if result['code'] != 0:
            body += "<p>{}</p>".format(time.asctime(time.localtime(time.time())))
            for key in result:
                body += "<p>{key}: {value}</p>".format(key=key, value=result[key])
            body += "<hr/>"
            sendMail(body)
            sys.exit(-1)
        del data["msg"]
        time.sleep(5)

def clockIn(cookies):
    url = "https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign"

    response = requests.get(url, headers=headers, cookies=cookies)

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
    result = json.loads(response.content.decode())
    mail += "<p>{}</p>".format(time.asctime(time.localtime(time.time())))
    mail = fun(result, mail)
    mail += "<hr/>"
    # sendMail(mail)

def main():
    # 获取Cookies文件内容
    with open(os.path.dirname(__file__) + "/cookies", "r") as f:
        string_cookies = f.read().split('\n')[0]

    # 格式化Cookies
    cookies = {}
    for i in string_cookies.split('; '):
        line = i.split('=')
        cookies[line[0]] = line[1]

    # 获取发送的信息
    try:
        msg = sys.argv[1]
    except IndexError:
        # 默认发送信息
        msg = send_string

    # 签到
    clockIn(cookies)
    # 给直播间发送信息
    sendMsg(msg, cookies)

if __name__ == "__main__":
    main()
