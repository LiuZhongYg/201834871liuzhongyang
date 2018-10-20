import os
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
porter_stemmer = PorterStemmer()
def wordtokenizer(sentence):
    word =WordPunctTokenizer().tokenize(sentence)
    return word

path="C:\\Users\\lzy\\Desktop\\20news-18828\\20news-18828"
dirs=os.listdir(path)
for file in dirs:
    dirs2=os.listdir(path+"\\"+file)
    for file2 in dirs2:
        i=0
        f=open(path+"\\"+file+"\\"+file2,errors='ignore')
        word=wordtokenizer(f.read())
        for w in word:
            word[i]=porter_stemmer.stem(word[i]) 
        
