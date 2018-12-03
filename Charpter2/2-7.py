#! usr/bin/env/python
# -*- coding:utf-8 -*-

# 从用户那里接受一个字符串输入，然后逐字符显示该字符串。先用while 循环实现，然后再用 for 循环实现

input_string = input('input_string')

print (u'使用while循环打印字符')
i = 0
while len(input_string)-i>0:
    print (input_string[i])
    i += 1

print (u'使用for循环打印字符')
for j in input_string:
    print (j)

