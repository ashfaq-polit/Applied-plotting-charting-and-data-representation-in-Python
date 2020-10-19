# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:31:00 2020

@author: mahme026
"""

#Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to Preview the Grading for each step #of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.

#This assignment requires that you to find at least two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of #weather phenomena (see below) for the region of Miami, Florida, United States, or United States more broadly.

#You can merge these datasets with data from different regions if you like! For instance, you might want to compare Miami, Florida, United States to Ann Arbor, USA. In that case #at least one source file must be about Miami, Florida, United States.

#You are welcome to choose datasets at your discretion, but keep in mind they will be shared with your peers, so choose appropriate datasets. Sensitive, confidential, illicit, #and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party #repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.

#Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple #visuals in different languages if you would like!

#As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s #principles of truth, beauty, function, and insight.

#Here are the assignment instructions:

#State the region and the domain category that your data sets are about (e.g., Miami, Florida, United States and weather phenomena).
#You must state a question about the domain category and region that you identified as being interesting.
#You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, #such as Wikipedia pages.
#You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, #functionality, beauty, and insightfulness.
#You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
#What do we mean by weather phenomena? For this category you might want to consider seasonal changes, natural disasters, or historical trends.

#Miqmi data: https://climatecenter.fsu.edu/climate-data-access-tools/downloadable-data
#Ann Arbor data: https://www.ncdc.noaa.gov/cdo-web/confirmation
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


