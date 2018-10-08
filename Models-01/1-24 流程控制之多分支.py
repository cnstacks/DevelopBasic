#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime    : 2018-10-08 19:01
# File    : 1-24 流程控制之多分支.py
# __author__: 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
编写一个猜测用户年龄的小游戏:
"""
age = 26
guess_age = int(input("Guess_age:"))

if guess_age > age:
    print("Try Smaller")
elif guess_age < age:
    print("Try Bigger")
else:
    print("恭喜你，猜对啦，可以抱得傻姑娘回家啦！")
