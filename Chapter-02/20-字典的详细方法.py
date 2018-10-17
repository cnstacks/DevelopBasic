#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-15 22:29
# File: 20-字典的详细方法.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
""
"""
存储更多的人的信息；
引出了字典的概念，类比新华字典！
"""
info = {}

# 增加
info['cxz'] = [24, 'male', '北京']
info['cxs'] = [24, 'male', 'shanghai']
info['cxl'] = [24, 'male', 'guangzhou']
info['cxy'] = [24, 'male', 'shenzhen']
print(info)

# keys
print(info.keys())

# values
print(info.values())

# items
print(info.items())

# clear
# info.clear()

#
info.setdefault('cxz', '崔晓昭')
print(info)

# 删除
del info['cxy']
print(info)

info.pop('cxl')
print(info)

info.popitem()
print(info)

# 修改
info['cxz'] = "cuixiaozhao"
print(info)

# 查询
print(info['cxz'])
print(info.get('cxs'))

#
c = info.copy()
print(c)
