#!/usr/bin/env python
# coding=utf-8

import os
import time

notice = False
warning = False
while True:
    charge = os.popen("acpi").read().split(', ')[1].split('%')[0]
    if int(charge) < 20 and not notice:
        notice = True
        os.system("st -e ~/.dwm/autostart/notice 电量不足 {}".format(charge))
    elif int(charge) < 10 and not warning:
        warning = True
        os.system("st -e ~/.dwm/autostart/notice 电量不足 {}".format(charge))
    elif int(charge) >= 20:
        notice = False
        warning = False
    time.sleep(30)
