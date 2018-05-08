# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:12:34 2018

@author: HantianZheng
"""
import pandas as pd
import numpy as np
import os
import scipy
import matplotlib.pyplot as plt
import tushare as ts
import time


#需要更新的数据
#pricedata: close, volume

start_date = '2011-01-04'
end_date = '2018-05-08'

#update price data
price_file_path = r'D:\大三下\投资学\模拟交易大作业说明\pricedata'
price_files = os.listdir(price_file_path)
#price_files = ['close.csv', 'volume.csv']
os.chdir(price_file_path)
close = pd.read_csv('close.csv',index_col = 0,parse_dates = True)
volume = pd.read_csv('volume.csv',index_col = 0,parse_dates = True)
last_date = str(close.index[-1])

add_close = pd.DataFrame() #不大好用 pd.date_range, 因为不知道那些天使交易日....
add_volume = pd.DataFrame()
#need to update the data from last date to end date
for stk in close.columns:
    print('stk : ',stk)
    stkdf = ts.get_k_data(stk,autype='hfq',start= last_date ,end = end_date)
    if stkdf.shape == (0,0):
        print('not exist... continue...')
        continue
    s = stkdf['close']
    s.index = stkdf['date']
    add_close[stk] = s
    s = stkdf['volume']
    s.index = stkdf['date']
    add_volume[stk] = s
    print('done...')
    
#output
tmp = pd.DataFrame(np.nan,index = add_close.index,columns = close.columns)
tmp[add_close.columns] = add_close
close_new = pd.concat([close,tmp])
close_new.to_csv('close.csv')
tmp = pd.DataFrame(np.nan,index = add_volume.index,columns = volume.columns)
tmp[add_volume.columns] = add_volume
volume_new = pd.concat([volume,tmp])
volume_new.to_csv('volume.csv')


