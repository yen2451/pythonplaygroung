# -*- coding: utf-8 -*-
# EnglishText_fileReadAndWrite.py
# @Author : chiayen hsu (yen_hsu's gmail:yen020224@gmail.com)
# @Date   : 8/18/2018, 11:10:27 AM
f1=open("englishText.txt",'r',1,encoding='utf8')
tex=f1.readlines()
f1.close()
for i in tex:
    print(i.strip())