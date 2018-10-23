#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: DevelopBasic 
# Software: PyCharm
# DateTime: 2018-10-23 10:17
# File: 5-三级菜单崔工版本.py
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

"""
1、循环字典对象；
2、使用列表保存中间状态，append及pop进行相对位置的存储与删除；
3、判断用户输入的值并给出提示语；
4、exit()方法退出程序：
"""
info = """
说明:输入q或Q退出程序,b或B返回上一层或首层菜单;
"""
current_layer, layers = (menu, [])
back_opt = ("B", "b")
exit_opt = ("Q", "q")

while 1:
    print(info)
    for key in current_layer: print(key)
    choice = input("请输入您的选项:").strip()
    if not choice: continue
    if choice in current_layer:
        layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice in back_opt:
        if len(layers) != 0:
            current_layer = layers.pop()
        else:
            print("已经回到第一层,请输入下级选项:")
    elif choice in exit_opt:
        exit("退出程序")
