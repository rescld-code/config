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
import requests

# 默认发送的消息
send_string = "打卡"

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
    { "id": "泠鸢yousa"          , "uid": 282994    , "roomid": 47377     } ,
    { "id": "hanser"             , "uid": 11073     , "roomid": 48743     } ,
    { "id": "三无Marblue"        , "uid": 284120    , "roomid": 544622    } ,

    { "id": "琉绮Ruki"           , "uid": 420249427 , "roomid": 21403609  } ,
    { "id": "七海Nana7mi"        , "uid": 434334701 , "roomid": 21452505  } ,

    { "id": "咩栗"               , "uid": 745493    , "roomid": 8792912   } ,
    { "id": "呜米"               , "uid": 617459493 , "roomid": 22384516  } ,

    { "id": "千春_Chiharu"       , "uid": 558070433 , "roomid": 22389319  } ,
    { "id": "田汐汐_Official"    , "uid": 473764233 , "roomid": 21627536  } ,
    { "id": "诗小雅Official"     , "uid": 36576761  , "roomid": 6129586   } ,
    { "id": "小美日语课堂"       , "uid": 52853477  , "roomid": 1720331   } ,

    { "id": "战斗吧歌姬官方账号" , "uid": 364225566 , "roomid": 14578426    , "msg": ("战斗吧歌姬，时刻回应爱！", False) },
]

string_cookies = ""
with open(os.path.dirname(__file__) + "/cookies", "r") as f:
    string_cookies = f.read().split('\n')[0]

url = "https://api.live.bilibili.com/msg/send"
MSG = "clock in"

data = {
    "color": 5566168,
    "fontsize": 25,
    "bubble": 0,
    "csrf_token": "14eda113da42f06e6b4b65c8a15e63e0",
    "csrf": "14eda113da42f06e6b4b65c8a15e63e0"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

cookies = {}
for i in string_cookies.split('; '):
    line = i.split('=')
    cookies[line[0]] = line[1]

def sendMsg():

    for i in live_room:
        try:
            if i["msg"][1]:
                data["msg"] = i["msg"][0]
            else:
                data["msg"] = MSG
        except KeyError:
            data["msg"] = MSG

        data["rnd"] = i["uid"]
        data["roomid"] = i["roomid"]

        response = requests.post(url, headers=headers, cookies=cookies,data=data)

        print("{}/{}\t{}".format(live_room.index(i)+1, len(live_room), i['id']))
        result = json.loads(response.content.decode())
        print(result)
        if result['code'] != 0:
            with open(os.environ['HOME'] + "/error", "a") as f:
                f.write(str(time.asctime(time.localtime(time.time()))) + "\n")
                f.write("bilibili send message error\n")
                json.dump(result, f)
                f.write("\n")
                f.write("-"*15 + "\n")
                exit(-1)
        print('-'*30)
        del data["msg"]
        time.sleep(5)

def clockIn():
    url = "https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign"

    response = requests.get(url, headers=headers, cookies=cookies)

    print(response.content.decode())

def main():
    global MSG
    try:
        MSG = sys.argv[1]
    except IndexError:
        MSG = send_string
    clockIn()
    sendMsg()

if __name__ == "__main__":
    main()

