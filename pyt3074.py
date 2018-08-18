# -*- coding: utf-8 -*-
# pyt3074.py
# @Author : chiayen hsu (yen_hsu's gmail:yen020224@gmail.com)
# @Date   : 8/18/2018, 9:56:44 AM
import os, shutil
if os.path.exists('files'):
    os.rmdir('files')
os.makedirs('files')
os.chdir('files')
i=int(input())
for x in range(1,i+1):
    x=int(x)
    ##^^i don't know