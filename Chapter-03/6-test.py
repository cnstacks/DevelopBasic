#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm2018.3
# DateTime: 2018-11-17 20:36
# File: 6-test.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

book = 0
Book =1
BOOK = 2
print(id(book))
print(id(Book))
print(id(BOOK))

我的名字 = 'cuixiaozhao'
print(我的名字)