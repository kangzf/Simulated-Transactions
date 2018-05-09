# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:41:46 2018

@author: HantianZheng
"""

#adaboost
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles
import os
import pandas as pd
'''
# 生成2维正态分布，生成的数据按分位数分为两类，500个样本,2个样本特征，协方差系数为2
X1, y1 = make_gaussian_quantiles(cov=2.0,n_samples=500, n_features=2,n_classes=2, random_state=1)
# 生成2维正态分布，生成的数据按分位数分为两类，400个样本,2个样本特征均值都为3，协方差系数为2
X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5,n_samples=400, n_features=2, n_classes=2, random_state=1)
#讲两组数据合成一组数据
X = np.concatenate((X1, X2))
y = np.concatenate((y1, - y2 + 1))

plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)

bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         algorithm="SAMME",
                         n_estimators=200, learning_rate=0.8)
bdt.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = bdt.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)
plt.show()
'''

#my code
main_path = r'D:\大三下\投资学\模拟交易大作业说明'
price_data_path = os.path.join(main_path,'pricedata')
report_data_path = os.path.join(main_path,'reportdata')
factors_path = os.path.join(main_path,'Factors')
wgt_path = os.path.join(main_path,'wgt')

os.chdir(price_data_path)
close = pd.read_csv('close.csv',index_col = 0,parse_dates = True)
rk = close.pct_change(5).shift(-5).rank(axis = 1,pct = True,ascending = True)
y = pd.DataFrame(np.nan,index = rk.index,columns = rk.columns)
y[rk >= 0.7] = 1
y[rk <= 0.3] = -1

facdf = pd.DataFrame()
os.chdir(factors_path)
for facname in os.listdir(factors_path):
    print(facname,' loading...')
    fac = pd.read_csv(facname,index_col = 0,parse_dates = True)
    fac = fac.rank(axis = 1,pct = True)  #input factor ranks
    facname = facname[:-4]
    facdf[facname] = fac.stack()

os.chdir(wgt_path)
wgt = pd.DataFrame(np.nan,index = close.index,columns = close.columns)
for i in range(wgt.shape[0]):
    if i <20:
        continue
    time_train = wgt.index[i-5]
    y_train = y.loc[time_train]
    y_train = y_train.dropna()
    #factor matrix for training
    facstack_train = facdf.loc[time_train,:]
    fac_train = pd.DataFrame(np.nan,index = close.columns,columns = facstack_train.columns)
    for facname in facstack_train.columns:
        fac_train[facname] = facstack_train[facname]
    fac_train = fac_train.loc[y_train.index,:]
    fac_train = fac_train.fillna(0)
    #construct the adaboost trees
    bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=3, min_samples_split=20, min_samples_leaf=10),algorithm="SAMME",n_estimators=100, learning_rate=0.8)
    bdt.fit(fac_train,y_train)
    #factor matrix now
    time_curr = wgt.index[i]
    facstack_curr = facdf.loc[time_curr]
    fac_curr = pd.DataFrame(np.nan,index = close.columns,columns = facstack_curr.columns)
    for facname in facstack_curr.columns:
        fac_curr[facname] = facstack_curr[facname]
    fac_curr = fac_curr.loc[y_train.index,:]
    fac_curr = fac_curr.fillna(0)
    pred_res = bdt.predict_proba(fac_curr)
    pred_res = pd.Series(pred_res[:,0],index = fac_curr.index)
    wgt.loc[time_curr,pred_res.index] = pred_res
    print(time_curr,' done...')
wgt.to_csv('wgt.csv')  
    



