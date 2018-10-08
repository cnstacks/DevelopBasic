#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# Time    : 2018-10-08 18:12
# File    : 1-21 格式化输出.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

""
"""打印个人信息的小程序！"""

# 方案01：
name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
hometown = input("Hometown:")

# print("------ Info of", name, "------")
# print("Name:", name)
# print("Age:", age)
# print("Job:", job)
# print("Hometown:", hometown)

# 方案02：
info = """
--------Info of %s -------
Name:%s
Age:%d
Job:%s
Hometown:%s
--------End of ------------
""" % (name, name, age, job, hometown)
print(info)


"""
小结：
1、input接收的数据类型都是"字符串"；
2、使用int()进行数据类型的转换！
"""