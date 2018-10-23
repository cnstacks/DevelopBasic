#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-23 09:36
# File: 3-装逼青年版.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
current_layer = menu
layers = []

while True:
    print("三级菜单程序".center(50, "*"))
    print("Usage:返回上一层请输入:b,退出程序请输入:q")
    print("三级菜单程序".center(50, "*"))
    for k in current_layer: print(k)
    choice = input(">>>:").strip()
    if not choice:
        continue
    elif choice == "b":
        if len(layers) != 0:
            current_layer = layers.pop()
        else:
            print("已经回到第一层，退出程序请输入:q")
    elif choice == "q":
        exit("退出该程序")
    if choice in current_layer:
        layers.append(current_layer)
        current_layer = current_layer[choice]
