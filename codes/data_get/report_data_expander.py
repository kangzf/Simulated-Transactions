# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:13:19 2018

@author: HantianZheng
"""
import pandas as pd
import numpy as np
import os
import scipy
import matplotlib.pyplot as plt
import tushare as ts

report_data_path = r'D:\大三下\投资学\模拟交易大作业说明\reportdata'
price_data_path = r'D:\大三下\投资学\模拟交易大作业说明\pricedata'

os.chdir(price_data_path)
close = pd.read_csv('close.csv',index_col = 0,parse_dates = True)

def choose_date(mydate,df):
    for i in range(1,10):
        trydate = mydate + str(i).zfill(2)
        if trydate in df.index:
            return trydate
    return ''    

os.chdir(report_data_path)
for reportfile in os.listdir(report_data_path):
    print(reportfile)
    reportdf = pd.read_csv(reportfile,index_col = 0,parse_dates = True)
    df = pd.DataFrame(np.nan,index = close.index,columns = close.columns)
    reportdf = reportdf.loc[:,reportdf.columns& close.columns]
    for time_curr in reportdf.index:
        time_curr_str = str(time_curr)
        year_curr = time_curr_str[:4]
        season_curr = time_curr_str[4:]
        if season_curr == '01':
            insert_date = year_curr + '06'
            insert_date = choose_date(insert_date,close)
        if season_curr == '02':
            insert_date = year_curr + '09'
            insert_date = choose_date(insert_date,close)  
        if season_curr == '03':
            insert_date = year_curr + '12'
            insert_date = choose_date(insert_date,close)      
        if season_curr == '04':
            insert_date = str(int(year_curr)+1) + '01'
            insert_date = choose_date(insert_date,close)   
        if insert_date != '':
            df.loc[insert_date,:] = reportdf.loc[time_curr,:]
        df = df.fillna(method = 'ffill')
        df.to_csv(reportfile)
    
    