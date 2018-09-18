# -*- coding: utf-8 -*-
import hashlib

string = '''
the stirng
Has many
line In
THE fIle
jb51 net
'''
# import
list_of_string = string.split()
print (list_of_string)  # 将字符串分离开，放入列表中
print ('*' * 50)


def case_insensitive_sort3(liststring):
    me=lambda x, y: x.lower()>y.lower()
    liststring.sort(me)


case_insensitive_sort3(list_of_string)
print (list_of_string)
