#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-10 21:29
# File: 09-列表类型.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
L1 = []  # 定义空列表;

print("L1:", L1)

L2 = list()  # 使用内置方法创建列表，但是不推荐该方法；
print("L2:", L2)

names = ["cuixiaozhao", "cuixiaoshan", "cuixiaosi", "cuixiaolei"]
print("Names:", names)

print(names[1])
print(names[2])
print(names[3])
# print(names[4])#IndexError: list index out of range
print(names[-1])
print(names[-2])
print("index:", names.index("cuixiaozhao"))

numbers = [1, 2, 3, 4, 5, 5, 5, 5, 3, 3, 3, 2, 2, 34, ]
names.extend(numbers)
print(names)
print(names[-5:])
print(names[-5:-1])
print(names[::2])  # ['cuixiaozhao', 'cuixiaosi', 1, 3, 5, 5, 3, 3, 2]
