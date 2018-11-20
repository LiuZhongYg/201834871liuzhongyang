from textblob import TextBlob
from textblob import Word
import numpy as np
import os
from nltk.corpus import stopwords
##def create_vsm_list():
##    voca_list=[]
##    with open("./vocabularies.txt","r") as voca:
##        words=voca.readlines()
##        for word in words:
##            word=word.strip('\n')
##            voca_list.append(word)
##    return voca_list

def data_process(path):
    flag=0
    list1_train={}
    list1_test={}
    dic_train = {}
    dic_test = {}

    b1=1
    b2=1
    global length
    length=[]

    log=0
        
    files=os.listdir(path)
    for file in files:
        list1_train={}
        txt_list=os.listdir(path+'/'+file)
        count=0
        for txt in txt_list:
            log+=1
            print(log)
            count=count+1
            with open(path+'/'+file+'/'+txt,'r',errors='ignore') as data:
                data_con=data.readlines()
                data_con=str(data_con).lower()
                data_con=TextBlob(str(data_con).replace("\\n","").replace("\\t","").replace("\\","").replace("'",""))
                data_con=data_con.words#分词

                filtered=[w for w in data_con if(w not in stopwords.words('english'))]
                for i in filtered:
                    w=Word(i)
                    w.lemmatize()
                    w.lemmatize('v')
                    for j in w:
                        if((j<'a'or j>'z')and j!='-'):
                            flag=1
                            break
                    if flag==1:
                        flag=0
                        continue
                    
                    if count<(0.9*len(txt_list)): #前90%分到训练集
                        if list1_train.get(w) is not None:
                            list1_train[w]+=1
                        else:
                            list1_train[w]=1
                    else:
                        if list1_test.get(w) is not None:
                            list1_test[w]+=1
                        else:
                            list1_test[w]=1
            if count>=(0.9*len(txt_list)):
                dic_test[file+"/"+txt]=list1_test
                if b1==1:
                    print(dic_test)
                    b1+=1
                list1_test={}
        
        length.append(count)
        dic_train[file]=list1_train
        if b2==1:
            print(dic_train)
            b2+=1
    return dic_train,dic_test

def NBC(dic_train,dic_test):
    acc=0
    log=0
    #length=0
##    for key2,value2 in dic_train.items():
##        length+=len(value2)
    for key,value in dic_test.items():
        p_max=-100000000000
        i=0
        log+=1
        print(log)
        for key2,value2 in dic_train.items():
            
            denomintor=0
            for key3 in value2:
                denomintor+=value2[key3] #该类中所有词语的次数
            denomintor+=len(value2)      #平滑处理，所以加上该类中词语的种类数
            p=0
            
            for feature in value.keys():
                if value2.get(feature) is not None:
                    numerator=value2[feature]+1#特征在该类中出现的次数+1
                else:
                    numerator=1#如果没出现，分子就为1
                p+=value[feature]*np.log(numerator/denomintor)#多项式模型
                #p +=np.log(numerator / denomintor)           #伯努利模型
            p+=np.log(length[i]/18828)
            
            if p>p_max:#取概率最大
                p_max=p
                index=key2
            i+=1        
        if index==key.split('/')[0]:
            acc+=1
    print(acc)
    print(len(dic_test))
    print(acc/len(dic_test))
if __name__=='__main__':
##  voca_list=create_vsm_list()
    dic_train,dic_test=data_process("./data/20news-18828")
    NBC(dic_train,dic_test)
    
