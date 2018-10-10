#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime    : 2018-10-08 19:53
# File    : 1-28 continue和break.py
# __author__: 天晴天朗
# Email   : tqtl@tqtl.org

count = 0
while count <= 10:
    print("Loop", count)
    if count == 5:
        break
    count += 1
print("----out of while loop1----")
count = 0
while count <= 10:
    count += 1
    if count == 5:
        continue
    print("Loop", count)

print("----out of while loop2----")
