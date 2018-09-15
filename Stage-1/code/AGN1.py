# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 00:28:40 2018

@author: rundo
"""
from pylab import *
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms


data = Table.read('data_all_PAH_removed.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
print(data.colnames)
print (len(data))


band4_5 = data['__4_5_']
band5_8 = data['__5_8_']
band3_6 = data['__3_6_']
band8_0 = data['__8_0_']
band24 = data['__24_']

a = band4_5-band8_0
b = band4_5
AGN_index = []

for i in range(0,len(data)):
    if band4_5[i] > 13.5:
        if a[i] >0.5:
            if (b[i]>13.5+(a[i]-2.3)/0.4):
                if data['e__3_6_'][i]<0.2:
                        if data['e__4_5_'][i]<0.2:
                            if data['e__5_8_'][i]<0.2:
                                if data['e__8_0_'][i]<0.2:
                                    if band4_5[i] > 14.5:
                                        AGN_index.append(i)
                                    if (b[i]> 14+(a[i]-0.5)):
                                        AGN_index.append(i)
                                    if (b[i] > 14.5-(a[i]-1.2)/0.3):
                                        AGN_index.append(i)

AGN = data[AGN_index]
AGN.write('AGN.fit')

data.remove_rows(AGN_index)
data.write('data_PAH&AGN_removed.fit')

plt.figure(figsize=(10,10))
plt.scatter(a,b,marker = '.')
plt.scatter(a[AGN_index],b[AGN_index], color = 'red')

plt.scatter(PAH1['__4_5_']-PAH1['__8_0_'],PAH1['__4_5_'],color='grey',marker='.')
plt.scatter(PAH2['__4_5_']-PAH2['__8_0_'],PAH2['__4_5_'],color='grey',marker='.')
plt.xlim(-2, 6)
plt.ylim(16, 4)
plt.xlabel('[4.5]-[8.0]')
plt.ylabel('[4.5]')
plt.title('AGN star')
