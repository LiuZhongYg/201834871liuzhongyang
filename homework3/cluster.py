import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn import metrics  # AMI值，评价聚类结果

from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, SpectralClustering,AgglomerativeClustering, FeatureAgglomeration, DBSCAN, Birch  # 进行聚类方法的获取
from sklearn.mixture import GaussianMixture

Data=[]
Labels=[]
Cluster=[]
def data_process():
    global Data
    with open("./Tweets.txt",'r') as data:
        data=data.readlines()
        for str in data:
            str=str.split("\"")
            Data.append(str[3])
            label=re.findall("\d+",str[6])[0]
            Labels.append(label)
            #print(str)
    tfidfvectorizer=TfidfVectorizer(tokenizer=word_tokenize,stop_words='english')
    Data=tfidfvectorizer.fit_transform(Data)
    #return Data
    #print(DataLabels)
def K_means():
    global Cluster
    Cluster =KMeans(n_clusters=110,random_state=10,).fit_predict(Data)
    print("K_means:")
    NMI()
def Affinity():
    global Cluster
    clu=AffinityPropagation().fit(Data)
    Cluster=clu.labels_
    print("Affinity:")
    NMI()
def Mean_shift():
    global Cluster
    Cluster=MeanShift().fit_predict(Data.toarray())
    print("Mean_shift")
    NMI()
def Spectral():
    global Cluster
    Cluster=SpectralClustering(n_clusters=110).fit_predict(Data)
    print("Spectral")
    NMI()
def WardHierarchicalCluster():
    global Cluster
    Cluster=AgglomerativeClustering(n_clusters=110).fit_predict(Data.toarray())
    print("WardHierarchicalCluster:")
    NMI()
def DBSCANClustering():
    global Cluster
    Cluster=DBSCAN(eps=1.13,min_samples=6).fit_predict(Data)
    print("DBSCANClustering:")
    NMI()
def Gaussian1():
    global Cluster
   # Cluster=GaussianMixture(n_compo=110).fit_predict(Data.toarray())
    Cluster=GaussianMixture(n_components=110).fit_predict(Data.toarray())
    print("Gaussianl:")
    NMI()
def Agglomerative():
    global Cluster
    Cluster=AgglomerativeClustering(n_clusters=110,linkage="average").fit_predict(Data.toarray())
    print("Agglomerative:")
    NMI()
def NMI():
    global Labels
    print("NMI:%s" % (metrics.normalized_mutual_info_score(Labels,Cluster)))
if __name__=='__main__':
    data_process()
    K_means()
    Affinity()
    Mean_shift()
    Spectral()
    WardHierarchicalCluster()
    DBSCANClustering()
    #Gaussian1()
    Agglomerative()