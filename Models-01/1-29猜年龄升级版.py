#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime    : 2018-10-08 20:01
# File    : 1-29猜年龄升级版.py
# __author__: 天晴天朗
# Email   : tqtl@tqtl.org


times = 0
age = 26  # 放在外侧，防止每次循环调用！

while times < 3:
    guess_age = int(input("GuessAge:"))
    if guess_age > age:
        print("Try Smaller")
    elif guess_age < age:
        print("Try Bigger")
    else:
        print("恭喜你，猜对啦！")
        break
    times += 1
    if times == 3:
        choice = input("没猜对，你还想继续吗？（Y|y）")  # 判断用户的结束节点；
        if choice == "y" or choice == "Y":
            times = 0  # 将计数器清空！
else:
    print("您已经猜测了%d次,次数已经用完，游戏结束啦！" % times)
