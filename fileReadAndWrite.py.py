# -*- coding: utf-8 -*-
# fileReadAndWrite.py.py
# @Author : chiayen hsu (yen_hsu's gmail:yen020224@gmail.com)
# @Date   : 8/18/2018, 10:25:44 AM
f1=open("text.txt",'r',1,encoding='utf8')
tex=f1.readlines()
f1.close()
print(tex)