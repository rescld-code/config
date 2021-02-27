#!/usr/bin/env python
# coding=utf-8

"""
    B站直播间上播提醒
    每5分钟检查一次
    python3 status.py uid
"""

import os
import sys
import time
import json
import requests

""" 战斗吧歌姬，时刻回应爱 """
UID = 364225566
LIVE_STATUS = 0

def getUserInfo(uid):
    url = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(uid)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.content.decode())["data"]

    # 信息提取
    info = dict()
    info["name"] = data["name"]
    info["live_status"] = data["live_room"]["liveStatus"]
    info["url"] = data["live_room"]["url"]
    return info

def main(uid):
    global LIVE_STATUS
    while True:
        info = getUserInfo(uid)
        if info["live_status"] == 1:
            if LIVE_STATUS == 0:
                LIVE_STATUS = 1
                # 弹窗提醒
                os.system("st -e ~/.config/awesome/autostart/notice {name}开播了 {url}".format(name=info["name"], url=info["url"]))
                # 自动打开直播间
                os.system("google-chrome-stable {}".format(info['url']))
        else:
            LIVE_STATUS = 0
        time.sleep(60 * 5)

if __name__ == "__main__":
    try:
        uid= sys.argv[1]
    except IndexError:
        uid = UID
    main(uid)
