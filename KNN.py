import math
import os
from textblob import TextBlob
from textblob import Word
#import numpy as np
dic_train={}
dic_test={}

def dis_compute(train,test):
    "用两个向量的余弦值度量相似性"
    dist=0
    fenzi=0
    fenmu1=0
    fenmu2=0
    
    for k in range(len(train)):
        fenzi+=train[k]*test[k]
        fenmu1+=train[k]*train[k]
        fenmu2+=test[k]*test[k]
    if fenmu1*fenmu2>0:
        return fenzi/((pow(fenmu1,0.5)*pow(fenmu2,0.5)))
    else:
        return 10000000
##def process(path):
##    "读取文件的vsm，返回一个字典，文件名：文件内容"
##    files=os.listdir(path)
##    dic={}
##    for file in files:
##        file_list=os.listdir(path+ "/" +file)
##        
##        for file_txt in file_list:
##            list=[]
##            data=open(path + "/" + file + "/" + file_txt,'r',errors='ignore')
##            data_output=data.readlines()
##            data_output=TextBlob(str(data_output).replace("\\n",""))
##            for i in data_output:
##                list.append(i)
##            dic[file_txt]=list;
##    return dic

def divide(percent,path):
    
    #首先划分训练集和测试集
  
    files=os.listdir(path)
    for file in files:
        file_list=os.listdir(path+ "/" +file)
        test_len=int(percent*len(file_list))
        
        for i in range(test_len):
            list1=[]
            txt=path + "/" + file + "/" + file_list[i]
            with open(txt,'r',errors='ignort') as f:
                data=f.readlines()
                for i in data:
                    temp=i.split(":")[1]
                    temp=temp.strip('\n')
                    list1.append(float(temp))
                dic_test[txt]=list1
        for i in range(len(file_list)-test_len):
            list1=[]
            txt=path + "/" + file + "/" + file_list[i+test_len]
            with open(txt,'r',errors='ignort') as f:
                data=f.readlines()
                for i in data:
                    temp=i.split(":")[1]
                    temp=temp.strip('\n')
                    list1.append(float(temp))
                dic_train[txt]=list1
                
def KNN(dic_train,dic_test,k):
    count_right=0
    count=0
    for test_key in dic_test.keys():  
        distance={}
        for train_key in dic_train.keys():
            test_vec=dic_test[test_key]
            train_vec=dic_train[train_key]
            
            d=dis_compute(test_vec,train_vec)
            distance[train_key]=d
        distance=sorted(distance.items(),key=lambda x:x[1],reverse=True)
        dic={}
        count+=1
        for i in range(k):
            if dic.get(distance[i][0].split("/")[2]) is None:
                dic[distance[i][0].split("/")[2]]=1
            else:
                dic[distance[i][0].split("/")[2]]+=1
        dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        
        if dic[0][0]==test_key.split("/")[2]:
            count_right+=1
    print("正确率："+str(count_right/count))
if __name__ == "__main__":
    path="./vsm/20news-18828"
    divide(0.2,path)
    KNN(dic_train,dic_test,10)
    
    
