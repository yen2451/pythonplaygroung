# -*- coding: utf-8 -*-
# sim.py
# @Author : chiayen hsu (yen_hsu's gmail:yen020224@gmail.com)
# @Date   : 8/18/2018, 11:16:50 AM
f1=open("./app/sim.txt",'r',1,encoding='gb2312')
tex=f1.readlines()
f1.close()
for i in tex:
    print(i.strip())