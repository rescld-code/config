#!/usr/bin/env python
# coding=utf-8

import os
import time

battery = ""  # 系统电量
batteryStatus = ""  # 充电状态
batteryWarned = False  # 是否已经提醒
batteryWarning = False  # 电量是否过低

def getBattery():
    # 获取电量与状态
    status = os.popen("acpi").read().split(' ')[2]
    if status == 'Not':
        battery = os.popen("acpi").read().split(' ')[4].split('\n')[0]
        batteryStatus = os.popen("acpi").read().split(' ')[3].split(',')[0]
    else:
        battery = os.popen("acpi").read().split(' ')[3].split(',')[0]
        batteryStatus = os.popen("acpi").read().split(' ')[2].split(',')[0]

    if int(battery.split('%')[0]) < 20 and batteryStatus == 'Discharging':
        batteryWarning = True
    else:
        batteryWarning = False

def notice():
    # 发出提示
    if batteryWarning == True and batteryWarned == False:
        batteryWarned = True
        os.system("st -e ~/.config/awesome/autostart/notice 电量不足....")
    elif batteryWarning == False:
        batteryWarned = False

def main():
    while True:
        getBattery()
        notice()
        time.sleep(30)

if __name__ == "__main__":
    main()
