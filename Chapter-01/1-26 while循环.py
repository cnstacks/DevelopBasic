#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime    : 2018-10-08 19:22
# File    : 1-26 while循环.py
# __author__: 天晴天朗
# Email   : tqtl@tqtl.org

num = 1
while num <= 100:
    if num == 50:
        pass
    elif num >= 60 and num <= 80:
        print("num*num:",num * num)
    else:
        print("Loop:", num)
    num += 1
