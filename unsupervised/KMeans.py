# -*-coding:utf-8-*-

"""
使用K-Means实现聚类

数据集:
    city.cvs -- 31省市居民家庭消费调查
介绍：
    现有1999年全国31个省份城镇居民家庭平均每人全年消费性支出的8个主要变量数据，这8个变量分别是：
    食品、衣着、家庭设备用品及服务、医疗保健、交通和通讯、娱乐教育文化服务、居住、杂项商品和服务。
目的：
    通过聚类，了解1999年各个省份的消费水平在国内的情况。
    将城市按照消费水平分为n_clusters个簇，消费水平相近的城市聚集在一个簇中。
K-Means的改进：
    计算两条数据相似性时，sklearn默认用的是欧式距离。
    虽然还有余弦相似度，马氏距离等多种方法，但没有设定计算距离方法的参数。
"""

import numpy as np
from sklearn.cluster import KMeans


def main():
    data, city_name = load_data('city.txt')
    # n_clusters指定聚类中心的个数
    km = KMeans(n_clusters=4)
    # 训练数据，获得标签序号。label聚类后个数据所属的标签序号。fit_predict()计算簇中心以及为簇分配序号
    label = km.fit_predict(data)
    # print(label) -- [1 3 2 2 2 2 2 2 1 0 3 0 3 2 2 2 0 0 1 0 0 3 0 2 0 3 2 2 2 2 2]
    # 聚类中心点的数值加和，也就是平均消费水平
    # 当axis为0时,是压缩行,即将每一列的元素相加,将矩阵压缩为一行
    # 当axis为1时,是压缩列,即将每一行的元素相加,将矩阵压缩为一列
    expenses = np.sum(km.cluster_centers_, axis=1)
    # print(expenses) -- [7754.65666667   4512.27375   5678.62   3788.758]
    # 将城市分为四类
    city_cluster = [[], [], [], []]
    # 将城市分按label分为设定的簇
    for i in range(len(city_name)):
        city_cluster[label[i]].append(city_name[i])
    # 将每个簇的城市输出，将每个簇的平均消费输出
    for i in range(len(city_cluster)):
        print("Expenses:%.2f" % expenses[i])
        print(city_cluster[i])
    pass


def load_data(file_path):
    """
    加载数据
    :param file_path: 文件路径
    :return: (城市的消费数据, 城市名)
    """
    fr = open(file_path, 'r+', encoding='utf-8')
    lines = fr.readlines()
    ret_data = []
    ret_city_name = []
    for line in lines:
        items = line.strip().split(",")
        ret_city_name.append(items[0])
        # 列表生成式
        ret_data.append([float(items[i]) for i in range(1, len(items))])
        # 等价形式
        # for i in range(1, len(items)):
        #     ret_data.append(float(items[i]))
    return ret_data, ret_city_name


if __name__ == '__main__':
    main()

"""
输出结果：

Expenses:3788.76
['河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '江西', '山东', '河南', '贵州', '陕西', '甘肃', '青海', '宁夏', '新疆']
Expenses:5678.62
['天津', '浙江', '福建', '重庆', '西藏']
Expenses:4512.27
['江苏', '安徽', '湖南', '湖北', '广西', '海南', '四川', '云南']
Expenses:7754.66
['北京', '上海', '广东']
"""
