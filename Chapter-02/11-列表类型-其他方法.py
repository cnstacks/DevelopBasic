#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-10 21:45
# File: 11-列表类型-其他方法.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
names_nums = ['cuixiaozhao', 'cuixiaoshan', 'X', 'I', 'A', 'O', 'Z', 'H', 'A', 'O', ' ', 'C', 'U', 'I', 'cuixiaolei', 1,
              3, 8, 1, 1, 2, 2, 1, 8, 9, 3, 1993, 9, 11, 136]

n = names_nums
# 指定某个元素进行删除;
n.remove('cuixiaozhao')
print(n)
# pop，删除最后一个；
n.pop()
print(n)
# 删除某个;
del n[2]
print(n)
# 删除一片;
del n[1:12]
print(n)
# for循环;
for i in n:
    print(i)
# range生成可迭代对象;
# range(0,10)
for i in range(10):
    print(i)

# while和for循环的区别？是否有循环边界;

# list的排序和反排序;
nums = list(range(10))
print(nums)
nums.append(138)
nums.append(24)
nums.append(14)
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)



# list的拼接或者拓展;
a= [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print(b)
print(a)
a.extend(b)
print(a)
print(b)
d = a.copy()
print(d)
