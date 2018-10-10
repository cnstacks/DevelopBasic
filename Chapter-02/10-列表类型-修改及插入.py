#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-10 21:39
# File: 10-列表类型-修改及插入.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
names_nums = ['cuixiaozhao', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 1, 3, 8, 1, 1, 2, 2, 1, 8, 9, 3, 1993, 9, 11]
n = names_nums
# list的追加;
n.append(136)
print(n)

# list的insert方法；
n.insert(3,'cuixiaoyan')
print(n)


# list的替换-重新赋值！
n[3]='cuiruochen'
print(n)

# list的批量修改;
n[2:4] = "XIAOZHAO CUI"
print(n)