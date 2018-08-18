# -*- coding: utf-8 -*-
# csvreader.py
# @Author : chiayen hsu (yen_hsu's gmail:yen020224@gmail.com)
# @Date   : 8/18/2018, 11:24:41 AM
f1=open("./app/stores_old.csv",'r',1,encoding='big5')
tex=f1.readlines()
f1.close()
for i in tex:
    print(i.strip())