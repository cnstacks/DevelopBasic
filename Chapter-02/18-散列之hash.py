#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-13 23:07
# File: 18-散列之hash.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

a = 1993
print(hash(a))

name = ("cuixiaozhao",)
print(hash(name))  # 2942107572806043745

nums = [1, 2, 3]
print(hash(nums))  # TypeError: unhashable type: 'list'


"""
用途:
1、文件签名；
2、md5加密；
3、密码验证；
"""