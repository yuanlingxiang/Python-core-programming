#! usr/bin/env/python
# -*- coding:utf-8 -*-

# 包含五个固定数值的列表或元组，输出他们的和。分别使用while 和for 循环实现

def str_to_int(num):
    return int(num)

list1 = input('数字间以逗号隔开，list1=').split(',')
list1 = list(map(str_to_int, list1))

print (list1)
list1_length = len(list1)

print (u'使用while循环实现')
list1_sum = 0
i = 0
while list1_length-i>0:
    list1_sum = list1[i] + list1_sum
    i += 1

print ('list1_sum=', list1_sum)

print (u'使用for循环实现')
list1_sum = 0
for j in list1:
    list1_sum = j + list1_sum

print ('list1_sum=', list1_sum)
