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

"""
小练习：
1、输入姓名、性别，判断如果是女生，打印我喜欢女生，否则，打印一起来搞基呀！
2、输入姓名、性别、年龄，判断如果是女生且年龄小于28岁，打印我喜欢女生，否则，打印姐弟恋也挺好的奥！
3、输入姓名、性别、年龄，判断如果是女生且年龄小于28岁，打印我喜欢女生，否则，打印姐弟恋也挺好奥！如果是男生，打印一起来搞基呀！
"""
# No.01
name = input("Name:")
gender = input("Gender:")
if gender == "female":
    print("我喜欢女生")
else:
    print("一起来搞基呀！")

# No.02
name = input("Name:")
gender = input("Gender:")
age = int(input("Age:"))
if gender == "female" and age < 28:
    print("我喜欢女生")

else:
    print("姐弟恋也挺好的！")

# No.03
name = input("Name:")
gender = input("Gender:")
age = int(input("Age:"))
if gender == "female" and age < 28:
    print("我喜欢女生")
elif gender == "male":
    print("打印一起来搞基呀！")
else:
    print("姐弟恋也挺好的！")
