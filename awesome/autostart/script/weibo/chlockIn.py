#!/usr/bin/env python
# coding=utf-8

"""
    微博超话自动签到
"""

import os
import time
import json
import requests

ids = [
    {"name": "泠鸢yousa"   , "id": "1008081acffb7516358bb316f0052fa9857be8"} ,
    {"name": "hanser"      , "id": "100808bb3bdea1fba9b8b940c3cb788d3f0aae"} ,
    {"name": "小缘"        , "id": "100808a06de9876f35084e6683073a63d9a947"} ,
    {"name": "三无marblue" , "id": "100808db2a58520ac2295a0a7a27903a53e34a"} ,

    {"name": "原神"        , "id": "100808fc439dedbb06ca5fd858848e521b8716"} ,
    {"name": "崩坏3"       , "id": "100808b2be6c70995a36f764be2790db0022f0"} ,
    {"name": "哔哩哔哩"    , "id": "100808502d8075299f18ee3773685119362071"} ,

    {"name": "战斗吧歌姬"  , "id": "100808f6d59f3ee3e0750d8a87d2895d7c5518"} ,
]

string_cookies = ""
with open(os.path.dirname(__file__) + "/cookies", "r") as f:
    string_cookies = f.read().split('\n')[0]

cookies = {}
for i in string_cookies.split('; '):
    line = i.split('=')
    cookies[line[0]] = line[1]

def main():
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
        "__rnd": "1613725339753"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "dnt": "1",
    }

    for i in ids:
        params["id"] = i["id"]
        headers["referer"] = "https://weibo.com/p/{}/super_inde".format(i["id"])
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        try:
            print(i["name"])
            print(json.loads(response.text))
        except Exception as e:
            with open(os.environ['HOME'] + "/error", "a") as f:
                f.write(str(time.asctime(time.localtime(time.time()))) + "\n")
                f.write("weibo clock in error\n")
                f.write(str(e) + "\n")
                f.write("-"*15 + "\n")
                exit(-1)
        time.sleep(1)

if __name__ == "__main__":
    main()
