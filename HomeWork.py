import os
import math
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords

porter_stemmer = PorterStemmer()

def wordtokenizer(sentence):                       #分词函数
    word =WordPunctTokenizer().tokenize(sentence)
    return word

def computeTF(alist):
    table={}
    for w in alist:
        if table.get(w,'never')=='never':   #统计各文本中各单词的频率
                table[w]=1
        else:
                table[w]+=1
                
    for k,v in table.items():               # TF normalization
            if table.get(k)>0:
                table[k]=(1+math.log(v))
    return table

def createVocabulary(alist):
    for w in alist:
        if w not in vocabulary:
            vocabulary.append(w)
            
def computeIDF():
    table={}
    for w in vocabulary:
        count=0
        for file in File:
            if file.get(elm,0)!=0:
                count+=1
        table[w]=count
    return table

def createVsm():
    for table in File:          #构建各文本的空间向量模型
        vsm=[]
        for elm in vocabulary:
            vsm.append(table.get(elm,0))
        vsmall.append(vsm)
    return vsmall

File=[]     #
vocabulary=[]    #词汇表

if __name__=='__main__':
    path="data\\20news-18828"
    dirs=os.listdir(path)
    for file in dirs:
        dirs2=os.listdir(path+"\\"+file)
        for file2 in dirs2:
            i=0
            f=open(path+"\\"+file+"\\"+file2,errors='ignore')
            word=wordtokenizer(f.read())
            for w in word:
                word[i]=porter_stemmer.stem(word[i])#标准化   
                i+=1
            filtered=[w for w in word if(w not in stopwords.words('english'))] #remove stopwords
            table=computeTF(filtered)
            createVocabulary(filtered)
            File.append(table)
                                                   
    table2=computeIDF(vocabulary,File)     #计算IDF
        
    for table in File:                          #TF*IDF
        for k,v in table.items():
            table[k]=v*math.log(len(File)/table2.get[k])
       
    vsmall=createVsm()

