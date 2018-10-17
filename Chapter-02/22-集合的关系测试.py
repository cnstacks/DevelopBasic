#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-16 17:28
# File: 22-集合的关系测试.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

""
"""
集合的关系测试：
交集：a.intersection(b)
差集:b.diffrence(c)
并集:c.union(d)
对称差集:d.symmetric_diffrence(e)
集合与集合之间的包含关系:
子集与超集：issubset、issuperset
集合是否相交：isdisjoint
"""
s = {1,2,3,4}
n = {2,3,5,6}

print(s & n)
print(s - n)
print(n-s)
print(s ^ n)
