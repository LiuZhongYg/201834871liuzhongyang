import os
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
porter_stemmer = PorterStemmer()
def wordtokenizer(sentence):                       #分词函数
    word =WordPunctTokenizer().tokenize(sentence)
    return word

path="C:\\Users\\lzy\\Desktop\\20news-18828\\20news-18828"
dirs=os.listdir(path)
File=[]     #
vocabulary=[]    #词汇表      
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
        table={}
        for w in filtered:
            if w not in vocabulary:
                vocabulary.append(w)            #构建词汇表
            if table.get(w,'never')=='never':   #统计各文本中各单词的频率
                table[w]=1
            else:
                table[w]+=1
        File.append(table)
        
#构建各文本的空间向量模型
vsmall=[]
for w in File:
    vsm=[]
    for elm in vocabulary:
        vsm.append(w.get(elm,0))
    vsmall.append(vsm)

