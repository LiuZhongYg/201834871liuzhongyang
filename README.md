# Data Mining Homework 
工程简介：
  一共包含六个文件：
  #vsm.py        用来构建向量空间模型
  #KNN.py        用来划分训练集、测试集，计算分类的正确率
  #data          原始数据
  #data_split    分词后的文本
  #vsm           生成的文本向量
  #vocabulary    字典
#
任务1：构建vsm
  首先对文本进行分词、去停用词等操作，计算每个单词的TF并使用Sub-linear TF scaling进行标准化，
然后计算每个单词的IDF，得到每个单词的权重，为了避免字典过大，设置权重阈值w_min进行过滤。
#
任务2：KNN
  按照一定比例划分训练集和测试集，使用向量间的余弦值度量相似性。计算测试集样本与训练集每个样本的相似度，
按相似度从大到小排序后，看排在前k个的训练集样本属于哪个类型的比较多，就把测试集样本分到哪个类型。

 
