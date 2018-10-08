#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime    : 2018-10-08 18:35
# File    : 1-23 流程控制语句.py
# __author__: 天晴天朗
# Email   : tqtl@tqtl.org
age_of_cxz = int(input("Please input your age:"))

if age_of_cxz > 25:
    print("It's time to Marry")
else:
    print("还可以再谈几次恋爱！")

USERNAME = "cuixiaozhao"
PASSWORD = "Ab123456."

username = input("Username:")
password = input("Password:")

if USERNAME == username and PASSWORD == password:
    print("Welcome %s to visit our Website." % USERNAME)
else:
    print("Wrong Username or Password You Input!")
