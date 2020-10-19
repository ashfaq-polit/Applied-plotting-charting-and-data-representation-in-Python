
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[ ]:

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df
df.head()


# In[ ]:




# In[ ]:

df_sorted = df.sort_values(by='Date')
df_sorted


# In[ ]:




# In[ ]:

df_reference = df_sorted[df_sorted['Date'] <= '2014-12-31']
df_reference


# In[ ]:




# In[ ]:

df_reference['Date'] = df_reference['Date'].str[5:]
df_reference


# In[ ]:

df_reference = df_reference.drop(df['Date']=='02-29')
df_reference


# In[ ]:

df_reference = df_reference[~df_reference.Date.str.contains("02-29")]
df_reference


# In[ ]:

df_compare = df_sorted[df_sorted['Date'] >'2014-12-31']
df_compare


# In[ ]:

df_compare['Date'] = df_compare['Date'].str[5:]
df_compare


# In[ ]:

df_gb = df_reference['Data_Value'].groupby([df_reference['Date']]).max()
df_gb = df_gb.reset_index()
df_gb


# In[ ]:

df_lb = df_reference['Data_Value'].groupby([df_reference['Date']]).min()
df_lb = df_lb.reset_index()
df_lb


# In[ ]:

df_gc = df_compare['Data_Value'].groupby([df_compare['Date']]).max()
df_gc = df_gc.reset_index()
df_gc
df_gc['Extreme'] = np.nan
df_gc


# In[ ]:

df_lc = df_compare['Data_Value'].groupby([df_compare['Date']]).min()
df_lc = df_lc.reset_index()
df_lc
df_lc['Extreme'] = np.nan
df_lc


# In[ ]:




# In[ ]:

range(len(df_gb))


# In[ ]:

for i in range(len(df_gb)):
    if df_gc['Data_Value'][i]>df_gb['Data_Value'][i]:
        df_gc['Extreme'][i] = df_gc['Data_Value'][i]
    if df_lc['Data_Value'][i]<df_lb['Data_Value'][i]:
        df_lc['Extreme'][i] = df_lc['Data_Value'][i]


# In[ ]:

df_lc
df_gc


# In[ ]:

#df_reference['Date'] = pd.to_datetime(df_reference['Date'], format='%Y-%m-%d') 


# In[ ]:




# In[ ]:

x = pd.Series(range(0,len(df_gb)))
x


# In[ ]:

get_ipython().magic('matplotlib notebook')


# In[ ]:

plt.plot(x,df_gb['Data_Value'],x,df_lb['Data_Value'],x,df_gc['Extreme'],'.',x,df_lc['Extreme'],'.')
plt.gca().fill_between(range(len(x)), 
                       df_gb['Data_Value'], df_lb['Data_Value'], 
                       facecolor='blue', 
                       alpha=0.25)
plt.xticks(np.linspace(0,365,13)[:-1], ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

plt.xlabel('Month of the Year')
plt.ylabel('Maximum & Minimum Temperature')
plt.title('Temperature change between 2015 & the previous Decade')

plt.legend(['Max temperature in 2005-2014', 'Min temperature in 2005-2014','Higher temperature in 2015','Lower temperature in 2015'])


