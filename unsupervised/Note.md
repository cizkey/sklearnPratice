# 无监督学习

* 有监督学习和无监督学习的最大区别在于数据是否有标签
* 无监督学习最常应用的场景是聚类(clustering)和降维(Dimension Reduction)

## 聚类(clustering)
* 聚类：根据数据的"相似性"将数据分为多类的过程
* 评估两个不同样本之间的"相似性"，通常使用的方法就是计算两个样本之间的"距离"。
* 使用不同的方法计算样本间的距离会关系到聚类结果的好坏。
* 常用聚类算法
    * K-Means
    * 近邻传播算法
    * DBSCAN
    * Gaussian Mixtures
    * Birch
* sklearn.cluster模块提供了各聚类算法函数实现

## 降维
* 降维：在保证数据所具有代表性特性或者分布的情况下，将高维数据转化为低维数据的过程
* 作用：数据的可视化，精简数据
* 常用降维算法
    * PCA
    * FastICA
    * NMF
    * LDA
* 降维过程也可以被理解为对数据的组成成分进行分解(decomposition)的过程，因此sklearn.decomposition模块提供了各降维函数实现


