#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-13 23:04
# File: 17-只读列表之元组.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


names = ("cuixiaozhao", "cuixiaoshan", "cuixiaosi", [11, 12, 13])
print(names[-1])
print(names[1:4])
names[-1][1] = "numbers"
print(names)  # ('cuixiaozhao', 'cuixiaoshan', 'cuixiaosi', [11, 'numbers', 13])
print(names.index('cuixiaozhao'))
"""
元组总结:
1、可切片；
2、index和count；
3、默认不可修改，但是元组内部如果包含可变类型，便可支持修改，如nums = [1,2,3,4]
4、一般用作配置文件；
"""