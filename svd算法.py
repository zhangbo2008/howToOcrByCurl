'''
下面代码是把图片看做二维矩阵点,然后做
svd压缩而已. 图片压缩算法.



因为推荐系统真实情况,用户的购买记录是一个稀疏矩阵,所以需要svd算法进行矩阵的化简,去除无用特征值.!
'''




# -*- coding: utf-8 -*-
'''
author@cclplus
date:2019/11/3
'''
import cv2
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


# 转为u8类型
def restore1(u, sigma, v, k):
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    a = np.dot(u[:, :k], np.diag(sigma[:k])).dot(v[:k, :])
    a[a < 0] = 0
    a[a > 255] = 255
    return np.rint(a).astype('uint8')

# 主入口函数, K表示暴露多少个特征值.
def SVD(frame, K=10):
    a = np.array(frame)
    # 由于是彩色图像，所以3通道。a的最内层数组为三个数，分别表示RGB，用来表示一个像素

    u_r, sigma_r, v_r = np.linalg.svd(a[:, :, 0])


    print(sigma_r,"特征值!!!!!!!!!!!!!,从结果看出来他已经经过排序了.")
    print(len(sigma_r),"特征值数量")  #下面按照3色图分别转化然后再拼起来成为图片即可.
    u_g, sigma_g, v_g = np.linalg.svd(a[:, :, 1])
    u_b, sigma_b, v_b = np.linalg.svd(a[:, :, 2])
    R = restore1(u_r, sigma_r, v_r, K)
    G = restore1(u_g, sigma_g, v_g, K)
    B = restore1(u_b, sigma_b, v_b, K)
    I = np.stack((R, G, B), axis=2)
    return I


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    frame = cv2.imread("./liuyifei.bmp")
    I = SVD(frame, 40)

    cv2.imwrite("out.bmp", I)
