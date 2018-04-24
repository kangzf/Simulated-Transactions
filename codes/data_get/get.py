# -*- coding: utf-8 -*-
import tushare as ts
import pandas as pd

df = ts.get_stock_basics()

##stocks = df.index.tolist()

# create output procedure
fpath='/Users/kangzifeng/Desktop/众课如繁星/大三下/双学位/投资学/模拟交易/Simulated Transactions/data/hist/data_all.xlsx'

writer = pd.ExcelWriter(fpath)

# basics
df.to_excel(writer,'basics',index=False)

# report data
##report = []
##for year in range(2010,2019):
##    for season in range(1,5):
##        report.append(ts.get_report_data(year, season))
##        # do other things
##
##pc=[]
##esp=[]
##bvps=[]
##pb=[]
##pc.to_excel(writer,'pc',index=False)
##esp.to_excel(writer,'esp',index=False)
##bvps.to_excel(writer,'bvps',index=False)
##pb.to_excel(writer,'pb',index=False)

writer.save()

