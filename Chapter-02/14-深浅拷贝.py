#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-11 12:17
# File: 14-深浅拷贝.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
""
"""
Python3中存在的深浅拷贝；
"""
# 变量举例:
a = 1
b = a
print("a:", a)
print("b:", b)
print("id(a):", id(a))
print("id(b):", id(b))
print("这里是分隔符".center(100, '-'))
a = 2
print("b:", b)
print("a:", a)
print("id(b):", id(b))
print("id(a):", id(a))
print("这里是分隔符".center(100, '-'))

# 列表举例:
names = ['cuixiaozhao', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan']
names2 = names
print("names:", names)  # names: ['cuixiaozhao', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan']
print("names2:", names2)  # names2: ['cuixiaozhao', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan']

print("names的id值:", id(names), "names2的id值:", id(names2))  # names的id值: 4422633096 names2的id值: 4422633096

print(id(names[1]), id(names2[1]))  # 4560274288 4560274288
names[0] = "崔晓昭"
print(names)
print(names2)
print("这里是分隔符".center(100, '-'))

print("此时的names:", names)  # 此时的names: ['崔晓昭', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan']
names_copy2 = names.copy()
print("names的浅拷贝之names_copy2:", names_copy2)
print("names的id值:", id(names), "names_copy2的id值:", id(names_copy2))
print(id(names[1]), id(names_copy2[1]))  # 4480082800 4480082800
print("这里是分隔符3".center(100, '-'))

names.append(['崔天晴', '崔天朗'])
names_copy2.append(['cxz', 'cxs'])
names_copy3 = names.copy()
print(names)
print(names2)
print(names_copy2)
print(names_copy3)
"""
['崔晓昭', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan', ['崔天晴', '崔天朗']]
['崔晓昭', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan', ['崔天晴', '崔天朗']]
['崔晓昭', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan', ['cxz', 'cxs']]
['崔晓昭', 'cuixiaoshan', 'cuixiaosi', 'cuixiaolei', 'cuixiaoyan', ['崔天晴', '崔天朗']]
"""
print(id(names))
print(id(names2))
print(id(names_copy2))
print(id(names_copy3))
"""
4410074760
4410074760
4410074824
4409935048
"""
names[-1][0] = "2020"
print(names)
print(names2)
print('-----------------***********--------------------------')
print(names_copy2)
print(names_copy3)
print('-----------------***********--------------------------')
print(id(names[-1][0]))
print(id(names2[-1][0]))
print(id(names_copy2[-1][0]))
print(id(names_copy3[-1][0]))
"""
4537801168
4537801168
4537800552
4537801168
"""

# 不建议使用deepcopy;
import copy

n4 = copy.deepcopy(names)
print(n4)
print(names)

print('----------------------')
names[-1][0] = 19930911
print(names)
print(n4)
print(id(names[-1][0]))
print(id(n4[-1][0]))
