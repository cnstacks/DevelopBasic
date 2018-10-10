#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime    : 2018-10-08 19:11
# File    : 1-25 打印分数的小程序.py
# __author__: 天晴天朗
# Email   : tqtl@tqtl.org


""
"""
 打印分数的小程序
"""
score = int(input("Please input your score:"))
if score > 100:
    print("最高分100，您可能输错了！")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 0:
    print("E")
else:
    print("滚，成绩没有负数！！！")
