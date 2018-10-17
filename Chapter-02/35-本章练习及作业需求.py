#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-17 09:30
# File: 35-本章练习及作业需求.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
""

# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝['alex', 'eric', 'rain']

names = ['cuixiaozhao', 'cuixiaoshan', 'cuixiaosi']

str_names = '_'.join(names)
print(str_names)

# 2、查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
list1 = list(tu)
list2 = list(dic.values())
list_all = li + list1 + list2
print(list_all)
for i in list_all:
    ret = i.strip()
    if (ret.startswith("a") or ret.startswith("A")) and ret.endswith("c"):
        print(ret)

# 3、写代码，有如下列表，按照要求实现每一个功能

li1 = ['alex', 'eric', 'rain', "eric", "eric"]

# 计算列表长度并输出
print(len(li1))
# 列表中追加元素“seven”，并输出添加后的列表
li1.append("seven")
print(li1)
# 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
li1.insert(1, "Tony")
print(li1)
# 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
li1[1] = "Kelly"
print(li1)
# 请删除列表中的元素“eric”，并输出修改后的列表
for i in li1:
    if i == "eric":
        li1.remove(i)
print(li1)
# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print(li1.pop(1), li1)
# 请删除列表中的第3个元素，并输出删除元素后的列表
del li1[2]
print(li1)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
del li1[1:4]
print(li1)
# 请将列表所有的元素反转，并输出反转后的列表
li1.append("cuixiaozhao")
li1.append("cxs")
li1.append("cxl")
li1.reverse()
print(li1)
# 请使用for、len、range输出列表的索引
for i in range(len(li1)):
    print(i)
# 请使用enumrate输出列表元素和序号（序号从100开始）
for index, item in enumerate(li1):
    print(item, index + 100)
# 请使用for循环输出列表的所有元素
for item in li1:
    print(item)
# 4、写代码，有如下列表，请按照功能要求实现每一个功能

li2 = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]

# 请根据索引输出“Kelly”
# 请使用索引找到'all'元素并将其修改为“ALL”，如：li[0][1][9]...
# 5、写代码，有如下元组，请按照功能要求实现每一个功能

tu2 = ('alex', 'eric', 'rain')

# 计算元组长度并输出;
print(len(tu2))
# 获取元组的第2个元素，并输出;
print(tu2[1])
# 获取元组的第1-2个元素，并输出;
print(tu2[0:2])
# 请使用for输出元组的元素;
for item in tu2:
    print(item)
# 请使用for、len、range输出元组的索引;
for index in range(len(tu2)):
    print(index)
# 请使用enumrate输出元祖元素和序号（序号从10开始）;
for index, item in enumerate(tu2):
    print(item, index)
# 6、有如下变量，请实现要求的功能

tu3 = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])

# 讲述元组的特性
"""
1、不可变类型；
2、可进行查询和切片；
3、可统计count以及index；
4、如果子元素是可变数据类型，则可修改；
"""
# 请问tu变量中的第一个元素“alex”是否可被修改？
"不可以"
# 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
"列表，可被修改，"
tu3[1][2]["k2"].append("Seven")
print(tu3)
# 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
"元组，不可修改"
# 7、字典
dic3 = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# 请循环输出所有的key
for key in dic3.keys():
    print(key)
# 请循环输出所有的value
for value in dic3.values():
    print(value)
# 请循环输出所有的key和value
for key, value in dic3.items():
    print(key, value)
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic3["k4"] = "v4"
print(dic3)
# 请在修改字典中“k1”对应的值为“alex”，输出修改后的字典
dic3["k1"] = "alex"
print(dic3)
# 请在k3对应的值中追加一个元素44，输出修改后的字典
dic3["k3"].append(44)
print(dic3)
# 请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
dic3["k3"].insert(0, 18)
print(dic3)
# 8、转换
# 将字符串s = "alex"转换成列表
s = "alex"
s_list = list(s)
print(s_list)
# 将字符串s = "alex"转换成元祖
s_tuple = tuple(s)
print(s_tuple)
# 将列表li = ["alex", "seven"]转换成元组
li_tuple = tuple(li)
print(li_tuple)
# 将元祖tu = ('Alex', "seven")转换成列表
tu_list = list(tu)
print(tu_list)
# 将列表li = ["alex", "seven"]转换成字典且字典的key按照10开始向后递增
li = ["alex", "seven"]
dic = {}
for item in li:
    a = len(li)
    a += 1
    dic[item] = a + 10
print(dic)

# 9、元素分类

# 有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
import time

start1 = time.time()
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic4 = {"k1": [], "k2": [], }
a = []
b = []
for num in nums:
    if num > 66:
        a.append(num)
    elif num < 66:
        b.append(num)
dic4["k1"] = a
dic4["k2"] = b
print(dic4)
end1 = time.time()
print(end1 - start1)

import time

start2 = time.time()
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
li.sort()  # 排序
z = li.index(66)
l = len(li)
dic = {"k1": li[z + 1:l], "k2": li[0:z]}
print(dic)
end2 = time.time()
print(end2 - start2)
# 即：{'k1':大于66的所有值, 'k2':小于66的所有值}

# 10、输出商品列表，用户输入序号，显示用户选中的商品

# 商品li = ["手机", "电脑", '鼠标垫', '游艇']
"""
允许用户添加商品;
用户输入序号显示内容;
"""
# 11、用户交互显示类似省市县N级联动的选择

# 允许用户增加内容
# 允许用户选择查看某一个级别内容

# 12、列举布尔值是False的所有值
{}, (), None, '', 0,
# 13、有两个列表

l1 = [11, 22, 33]
l2 = [22, 33, 44]

# 获取内容相同的元素列表
s1 = set(l1)
s2 = set(l2)
print(s1, s2)
# 获取l1中有，l2中没有的元素列表
s1_s2 = s1 - s2
print(s1_s2)

# 获取l2中有，l1中没有的元素列表
s2_s1 = s2 - s1
print(s2 - s1)
# 获取l1和l2中内容都不同的元素
s1s2 = s1 ^ s2
print(s1s2)

# 14、利用For循环和range输出

# For循环从大到小输出1 - 100
for num in range(100, 0, -1):
    print(num)
# For循环从小到到输出100 - 1
for num in range(1, 101):
    print(num)
# While循环从大到小输出1 - 100
num = 1
while num < 101:
    print(num)
    num += 1
# While循环从小到到输出100 - 1
num = 100
while num > 0:
    print(num)
    num -= 1
# 在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]
li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
li.sort()
print(li)
print(li[-1])
# 在不改变列表中数据排列结构的前提下，找出以下列表中最接近最大值和最小值的平均值 的数li = [-100,1,3,2,7,6,120,121,140,23,411,99,243,33,85,56]
li = [-100, 1, 3, 2, 7, 6, 120, 121, 140, 23, 411, 99, 243, 33, 85, 56]
li.sort()
print(li)
avg = (li[0] + li[-1]) / 2
lte = []
gte = []
print(avg)
for item in li:
    if item > avg:
        gte.append(item)
    elif item < avg:
        lte.append(item)
print(gte, lte)
if abs(avg - gte[0]) < abs(avg - lte[-1]):
    print("最接近的数值为：", gte[0])
elif abs(avg - gte[0]) > abs(avg - lte[-1]):
    print("最接近的数值为：", lte[-1])
# 利用for循环和range输出9 * 9乘法表
print('\n'.join([' '.join(["%d*%d=%2s" % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))

# 求100以内的素数和。（编程题）

sum = 0
for num in range(1, 100):
    # 质数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            sum += num
print(sum)
