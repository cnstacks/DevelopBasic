#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-10 22:19
# File: 12-列表练习题讲解.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

# 1、创建一个空列表，命名为names，往里面天添加old_driver，rain，jack，shanshan，peiqi，black，black_girl元素；
names = []
names.append("old_driver")
names.append("rain")
names.append("jack")
names.append("shanshan")
names.append("peiqi")
names.append("black")
names.append("black_girl")
print("No.01:", names)  # No.01 ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black', 'black_girl']

# 2、往names列表里black_girl前面插入一个alex;
names.insert(names.index("black_girl"), "alex")
print("No.02:", names)  # No.02: ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black', 'alex', 'black_girl']

# 3、把shanshan的名字改成中文"姗姗";

names[names.index("shanshan")] = "姗姗"
print("No.03:", names)  # No.03: ['old_driver', 'rain', 'jack', '姗姗', 'peiqi', 'black', 'alex', 'black_girl']

# 4、往names列表里rain的后面插入一个子列表["oldboy", "oldgirl"]
names.insert(names.index("rain") + 1, ["oldboy", "oldgirl"])
print("No.04:", names)
# No.04: ['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', '姗姗', 'peiqi', 'black', 'alex', 'black_girl']

# 5、返回peiqi的索引;
print("No.05:", names.index("peiqi"))  # No.05: 5

# 6、创建新列表[1,2,3,4,2,5,6,2]，合并入names列表;
nums = list(range(1, 5))
nums.append(2)
nums.append(5)
nums.append(6)
nums.append(2)
combine = names + nums
print("No.06:", combine)  #
# No.06: ['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', '姗姗', 'peiqi', 'black', 'alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]

# 7、取出names列表中索引4-7的元素
print("No.07:", names[4:8])  # No.07: ['姗姗', 'peiqi', 'black', 'alex']
#
# 8、取出names列表中索引2-10的元素，步长为2
print("No.08:", names[2:11:2])  # No.08: [['oldboy', 'oldgirl'], '姗姗', 'black', 'black_girl']

# 9、取出names列表中最后3个元素;
print("No.09:", names[-3:])  # No.09: ['black', 'alex', 'black_girl']
print("此处为分隔符0".center(120, '-'))
# 10、循环names列表，打印每个元素的索引值和元素;

# 方法01：
count = 0
for name in names:
    print("No.10-1", count, name)
    count += 1
"""
0 old_driver
1 rain
2 ['oldboy', 'oldgirl']
3 jack
4 姗姗
5 peiqi
6 black
7 alex
8 black_girl
"""
print("此处为分隔符1".center(120, '-'))
# 方法02：enumerate(names) 枚举；
print(enumerate(names))  # 直接取索引，<enumerate object at 0x107a17a68>
for name in enumerate(names):
    print("No.10-2", name)  # 打印的值是一个小列表
print("此处为分隔符2".center(120, '-'))
"""
(0, 'old_driver')
(1, 'rain')
(2, ['oldboy', 'oldgirl'])
(3, 'jack')
(4, '姗姗')
(5, 'peiqi')
(6, 'black')
(7, 'alex')
(8, 'black_girl')
"""
for index, name in enumerate(names):
    print("No.10-3", index, name)  # 打印的值不是列表了
print("此处为分隔符3".center(120, '-'))
"""
0 old_driver
1 rain
2 ['oldboy', 'oldgirl']
3 jack
4 姗姗
5 peiqi
6 black
7 alex
8 black_girl
"""
# 11、循环names列表，打印每个元素的索引值和元素，当索引值为偶数，把对应的元素改成-1
for index, name in enumerate(names):
    if index % 2 == 0:  # 代表偶数
        names[index] = -1
        print("No.11", index, name)  # 打印的值不是列表了;
print("No.11", names)
print("此处为分隔符".center(120, '-'))
# # 12、names里有3个2，请返回第2个2的索引值，不要人肉数，要动态找（提示，找到第一个2的位置，在此基础上再找第2个）

# 方法一：
names = ['cuixiaozhao', 2, 'cuixiaoshan', 'cuixiaosi', 2, 'cuixiaolei', 1, 3, 4, 2]
count = 0
for i in names[names.index(2) + 1:]:
    if i == 2:
        print("第二个2的index:", names.index(2) + 1 + count)
        break
    count += 1
# 方法二:
first_index = names.index(2)  # 第一个2的索引值
new_list = names[first_index + 1:]  # 从第一个2的位置+1 开始切片，重新赋值给新的列表
second_index = new_list.index(2)  # 查询2 在新的列表中的索引值
last_index = first_index + second_index + 1  # 第一个的索引值+ '第二个的索引值+切片时候的+1'
print("第二个2 的index:", last_index)

# 13、现有商品列表如下：
products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
"""
需打印出这样的格式
---------商品列表----------
0. Iphone8    6888
1. MacPro    14800
2. 小米6    2499
3. Coffee    31
4. Book    80
5. Nike Shoes    799
"""
print("商品列表".center(60, '-'))
for index, product in enumerate(products):
    # print("%s %s %s" % (str(index) + ".", product[0], product[1]))
    print("%s. %s %s" % (index, product[0], product[1]))

# 14、写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购物车里边的商品列表
shopping_cart = []
while True:
    for index, product in enumerate(products):
        print("%s. %s %s" % (index, product[0], product[1]))
    want = input("您想要买什么，请输入对象商品编号： 例<2>,输入<q>退出 >>")
    if want.isdigit():
        want = int(want)
        if want > len(products) - 1 and want < 0:
            print("输入商品编号错误，没有该编号!!")
        else:
            shopping_cart.append(products[want])
            print("已经将%s加入购物车" % products[want])
    elif want == "q":
        if len(shopping_cart) > 0:
            print("您已购买以下商品：")
            for index, i in enumerate(shopping_cart):
                print("%s. %s %s" % (index, i[0], i[1]))
        break
    else:
        print("输入不正确！")
        continue

# 知识补充：

# 判断字符串是否是一个数字;
"33".isdigit()

# 查看列表的长度;
len(names)

# break 退出也可以用标志位来设置True False 进行循环判断退出;
# 标志位;
flag = True
while flag:
    if 100:
        pass
    else:
        flag = False  # 标志位 设置False 结束循环;
