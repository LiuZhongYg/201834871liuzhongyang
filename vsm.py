import os
import math
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords

def data_process1(path,path2):
    "分词，去停用词,然后存起来"
    vocabulary=[]
    list=[]
    files=os.listdir(path)
    for file in files:
        file_list=os.listdir(path+ "/" +file)
        for file_txt in file_list:
            data=open(path + "/" + file + "/" + file_txt,'r',errors='ignore')
            data_con=data.readlines()
            data_con=str(data_con).lower()
            data_con=TextBlob(str(data_con).replace("\\n","").replace("\\t","").replace("\\","").replace("'",""))
            data_con=data_con.words#分词
            
            
            filtered=[w for w in data_con if(w not in stopwords.words('english'))]#去停用词
            dic={}
            for i in filtered:
                w=Word(i)
                w.lemmatize()
                w.lemmatize('v')
                if dic.get(w) is not None:
                    dic[w]+=1
                else:
                    dic[w]=1
##                if w not in vocabulary:
##                    vocabulary.append(w)  #初步建立词汇表
               
            for k,v in dic.items():
                    dic[k]=(1+math.log(v))#标准化tf
            list.append(dic)
##            with open(path2+"/"+file+"/"+file_txt,'w+') as f:   
##                for k,v in dic.items():
##                    f.write(k+":"+str(v)+"\n")                      
##    with open("./vocabulary.txt",'w+') as f:
##        for i in vocabulary:
##            f.write(str(i)+"\n")
    return list
##def data_stem_if(path):
##    "还原单词，计算频率,标准化频率并存起来,初步建立词汇表"
####    count1=0
####    count2=0
####    
##    vocabulary=[]
##    list=[]#
##    files=os.listdir(path)
##    for file in files:
##        file_list=os.listdir(path+ "/" +file)
##        for file_txt in file_list:
##            data=open(path + "/" + file + "/" + file_txt,'r',errors='ignore')
##            data_con=data.readlines()
##        
##            data=TextBlob(str(data_con).replace("\\n","").replace("'",""))
##            data=data.words
##            #print(data)
##            dic={}
##            for i in data:
##
##                #print(i)
##                
##                w=Word(i)
##                w.lemmatize()
##                w.lemmatize('v')
##                if dic.get(w) is not None:
##                    dic[w]+=1
##                else:
##                    dic[w]=1
##                    
##                #print(w)
##               # count1=1
##               # break
##            
####                if w not in vocabulary:
####                    vocabulary.append(w)  #初步建立词汇表
####
####            if count1==1:
####                count2=1
####                break
####        if count2==1:
####            break
##            for k,v in dic.items():
##                if dic[k]>0:
##                    dic[k]=(1+math.log(v))
##            #list.append(dic)
##            with open(path+"/"+file+"/"+file_txt,'w+') as f:
##                for key in dic.keys():
##                    f.write(key+"\n")
####    with open("./vocabulary.txt",'w+') as f:
####        for i in vocabulary:
####            f.write(str(i)+"\n")
##    print("ok")
##    #return list
##

def data_process2(data,w_min):
    "数据来自data_stem_if()"
    table={}
    data1=data
    vocabulary=[]#修改
    with open("./vocabulary.txt",'r') as f:
        data_con=f.readlines()
        data_con=TextBlob(str(data_con).replace("\\n","").replace("'","").replace("\\t","").replace("\\",""))
        data_con=data_con.words
        for i in data_con:
           
            count=0
            for file in data:
                if file.get(i,0)!=0:
                    count+=1
            table[i]=count
               
    for file in data:
        for k,v in file.items():                 
            if table.get(k,0)!=0:
                file[k]=v*math.log(len(data)/table[k])
                if file[k]>=w_min and (k not in vocabulary):
                    vocabulary.append(k)
       
    index=0    
    with open("./vocabulary.txt",'w+') as f:
        for i in vocabulary:
            f.write(str(i)+"\n")
            index+=1
    print(index)
    return vocabulary,data
def help(path):
    list=[]
    files=os.listdir(path)
    for file in files:
        file_list=os.listdir(path+ "/" +file)
        for file_txt in file_list:
            data=open(path + "/" + file + "/" + file_txt,'r',errors='ignore')
            data_con=data.readlines()
            for i in data_con:
                ch=i.split(":")[0]
                if ch not in list:
                    list.append(ch)
    index=0
    with open("./vocabulary.txt",'w+') as f:
        for i in list:
            f.write(str(i)+"\n")
            index+=1
    print(index)
def create_vsm(path,data,vocabulary):
    "建立向量空间模型"
    count=0
    files=os.listdir(path)
    for file in files:
        file_list=os.listdir(path+ "/" +file)
        for file_txt in file_list:
            with open(path + "/" + file + "/" + file_txt,'w+') as f:
                for word in vocabulary:
                    if data[count].get(word,0)!=0:
                        f.write(word+":"+str(data[count][word])+"\n")
                    else:
                        f.write(word+":"+"0"+"\n")
            count+=1
def count():
    with open("./vocabulary.txt",'r') as f:
        data=f.readlines()
        print(len(data))
    

if __name__ == "__main__":

    #help("./data_process/20news-18828")
    list1=data_process1("./data/20news-18828","./data_process/20news-18828")
    list2,list3=data_process2(list1,20)
    create_vsm("./vsm/20news-18828",list3,list2)
    print("ok")
    
    
   
        
            
