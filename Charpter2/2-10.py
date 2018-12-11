#! usr/bin/env/python
# -*- coding:utf-8 -*-
"""
使用raw_input()函数来提示用户输入一个1和100之间的数，如果用户输入的数满足这个条件，
显示成功并退出。否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止
"""

while True:
    num = int(input(u'输入0~100之间的数：'))
    if num in range(0, 101):
        print ('num:', num)
        break
    else:
        print (u'输入的数据不正确， 重新输入')
        continue
