#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-13 22:42
# File: 16-字符串的方法02.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

s1 = "Hello World!"
print(s1.index('o'))

s2 = '19930911'.isalnum()
s2_1 = 'cxz1990911'.isalnum()
s2_2 = 'cxz19930911@#$%'.isalnum()
print(s2, s2_1, s2_2)

s3 = '1993'.isalpha()
print(s3)

s4 = '33'.isdecimal()
s4_1 = '33.3'.isdecimal()
print(s4, s4_1)

s5 = '333'.isdigit()
print(s5)

s6 = '333d'.isidentifier()
print(s6)  # False

s7 = 'cxz19930911'.islower()
s7_1 = '19930911cXS'.islower()
print(s7, s7_1)

s8 = '19930911cxs'.isnumeric()
print(s8)

s9 = '33'.isprintable()
print(s9)

s10 = 'Chery Man'.istitle()
print(s10)

names = ['cuixiaozhao', 'cuixiaoshan', 'cuixiaosi']
s11 = ''.join(names)
s11_1 = '**'.join(names)
print(s11)
print(s11_1)

s12 = "Hello World!"
s12_1 = s12.ljust(50, "-")
print(s12_1)

s13 = "CUIXIAOZHAO"
print(s13.lower())
s13_1 = "cxz"
print(s13_1.upper())

s14 = "    Hello World!   "
print(s14.lstrip())
print(s14.rstrip())

str_in = "abcde"
str_out = "!@#$%"
table = str.maketrans(str_in, str_out)
print(table)  # {97: 33, 98: 64, 99: 35, 100: 36, 101: 37}

deco = "cuixiaozhao".translate(table)
print(deco)  ##uixi!ozh!o

s15 = "hello world"

print(s15.partition('o'))
print(s15.rpartition('o'))

s16 = "cuixiaozhao"
print(s16.replace("xiaozhao", "tianqing"))
print(s16.replace("xiaozhao", "tianqing", 2))

s17 = "hello world"
print(s17.rfind('o'))

s18 = "cuixiaozhao"
print(s18.startswith('c'))
print(s18.endswith('123'))

s19 = "cuixiaozhao"
print(s19.zfill(40))

"""
isdigit
replace
find 
count
split
strip
index
center
format
join 
"""
