#coding:utf-8
import os 
import linecache  
import json
from itertools import islice

root = 'D:\\01DELFI\\DELFI\\Dataiku\\new-york-city-taxi-fare-prediction\\train.csv' 
f=open(root)
data = f.readlines()
total_line = len(data)
print(total_line)
chunks=total_line//500000;

# 读取 第一行到第十行内容
#print(data[0:10])
for i in range(chunks+1):
    start=(i)*500000
    end=start+500000
    f_out = open("D:\\01DELFI\\DELFI\\Dataiku\\new-york-city-taxi-fare-prediction\\train_data_split\\data"+str(i), "w+")
    #for i in range(len(data[start:end])):
    #    f_out.writelines(str(data[i])) 
    f_out.writelines(data[start:end]) 
    f_out.close()   
    print(str(start)+"-"+str(end));  

f.close()
