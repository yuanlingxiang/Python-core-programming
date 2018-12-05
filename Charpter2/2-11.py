#! usr/bin/env/python
# -*- coding:utf-8 -*-
"""
写一个带文本菜单的程序，
菜单项如下：
(1)取五个数的和
(2) 取五个数的平均值....
(X)退出
由用户做一个选择，然后执行相应的功能。当用户选择退出时程序结束
"""

def get_sum(nums):
    return sum(nums)

def get_avg(nums):
    return get_sum(nums)/len(nums)*1.0

def get_exit(*args):
    return exit(0)

list1 = []
func_dict = {'(1)':get_sum, '(2)':get_avg, 'X':get_exit}
for num in range(1, 6):
    list1.append(int(input(u'输入第%s个数：' % num)))

print (u'(1)取五个数的和')
print (u'(2) 取五个数的平均值....')
print (u'(X)退出')

while True:
    option = input(u'make a choice:')
    if func_dict.get(option):
        print (func_dict.get(option)(list1))



