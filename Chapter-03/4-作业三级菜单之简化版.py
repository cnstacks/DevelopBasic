#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "tqtl"
# Date:2018/5/13 23:06
# 需求：
# 可依次选择进入各子菜单；
# 可从任意一层往回退到上一层；
# 可从任意一层退出程序；
# 所需新知识点：列表、字典；
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
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
current_layer, layers = (menu, [])  # 定义变量current_layer,layers;
while True:
    for keys in current_layer: print(keys)  # 合成一层展示；
    choice = input(">>>:").strip()  # strip方法去除多余字符；
    if not choice: continue  # 简化写法，省一行代码；
    if choice in current_layer:
        layers.append(current_layer)
        current_layer = current_layer[choice]  # 虽说省去一行代码，但是Python风格规范不建议这么书写；
    elif choice == 'b':  # 使用b代表回退一层，back的缩写；
        if len(layers) != 0:  # 层数为0时候pop()方法会报错，添加判断；
            current_layer = layers.pop()
        else:
            print("Back to the first floor.")
    elif choice == 'q':  # 使用b代表退出程序，quit的缩写；
        exit("exit the three layers menu program.")
