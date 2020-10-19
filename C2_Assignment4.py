# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:31:00 2020

@author: mahme026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_miami = pd.read_csv('miami_weather.txt' , sep=',')
    
df_miami
df_miami = df_miami.drop(df_miami.columns[[0]], axis=1) 
df_miami.columns = ['Year','Month','Day','Precipitation','Max temp','Min temp','Mean temp']

#if df_miami[Month]==2 & df_miami['Day']==29:
#    if df_miami:
        
df_miami = df_miami[~ ((df_miami['Month']==2) & (df_miami['Day']==29) & (df_miami['Year']/4)!=0)]

#df_miami['Date'] = pd.to_datetime(df_miami[['Year', 'Month', 'Day']]).str()

import datetime as dt
df_miami['Date'] = df_miami.apply(lambda x: dt.datetime(x['Year'], x['Month'], x['Day']), axis=1)

df_miami = df_miami.drop(df_miami.columns[[0,1,2]], axis=1) 
#df_miami['Date'] = df_miami['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
df_miami = df_miami.replace(-99.9, np.nan)
#df_miami.columns = ['Date','Precipitation','Max temp','Min temp','Mean temp']


df_ann_arbor = pd.read_csv('ann_arbor_weather.csv')

df_ann_arbor 
df_ann_arbor['DATE'] = pd.to_datetime(df_ann_arbor['DATE'])

df_merged = pd.merge(df_miami,df_ann_arbor,how='inner',left_on='Date',right_on='DATE')

plt.figure()
#observation_dates = np.arange(df_merged['Date'][0], df_merged['Date'][len(df_merged)-1], dtype='datetime64[D]')
#observation_dates = list(map(pd.to_datetime, observation_dates)) # convert the map to a list to get rid of the error
plt.subplot(1, 2, 1)
ax1 = plt.plot(df_merged['Date'], df_merged['Min temp'], df_merged['Date'], df_merged['Max temp'])

plt.subplot(1, 2, 2,sharey=ax1)
ax2 = plt.plot(df_merged['Date'], df_merged['TMIN'], df_merged['Date'], df_merged['TMAX'])
plt.show

fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)
fig.suptitle('Weather comparison betn Maimi & Ann Arbor in terms of Temperature')
ax1.plot(df_merged['Date'], df_merged['Min temp'], df_merged['Date'], df_merged['Max temp'])
ax1.set_title('Miami')
ax1.legend(['Min temp', 'Max temp'])
ax1.set(ylabel="Temperature")
ax2.plot(df_merged['Date'], df_merged['TMIN'], df_merged['Date'], df_merged['TMAX'])
ax2.set_title('Ann Arbor')
ax2.legend(['Min temp', 'Max temp'])


