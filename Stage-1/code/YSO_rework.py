# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:01:48 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransform

data = Table.read('data_PAH&ANG&shock&PAHcon_removed.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')
shock = Table.read('shock.fit')
PAHcon = Table.read('PAHcon.fit')


x = data['__4_5_']-data['__5_8_']
y = data['__3_6_']-data['__4_5_']

YSO_index = []


for i in range(0,len(data)):
    if x[i] > 0.7:
        if y[i] > 0.7:
            if data['e__3_6_'][i]<0.2:
                if data['e__4_5_'][i]<0.2:
                    if data['e__5_8_'][i]<0.2:
                        if data['e__8_0_'][i]<0.2:
                                YSO_index.append(i)
                                
data[YSO_index].write('YSO.fit')                                

                                
plt.figure(figsize=(10,10))

plt.scatter(x,y)
plt.scatter(x[YSO_index],y[YSO_index], color = 'b')

plt.scatter(PAH1['__4_5_']-PAH1['__5_8_'],PAH1['__3_6_']-PAH1['__4_5_'],color='grey',marker='.')
plt.scatter(PAH2['__4_5_']-PAH2['__5_8_'],PAH2['__3_6_']-PAH2['__4_5_'],color='grey',marker='.')
plt.scatter(AGN['__4_5_']-AGN['__5_8_'],AGN['__3_6_']-AGN['__4_5_'],color='grey',marker='.')
plt.scatter(shock['__4_5_']-shock['__5_8_'],shock['__3_6_']-shock['__4_5_'],color='grey',marker='.')
plt.scatter(PAHcon['__4_5_']-PAHcon['__5_8_'],PAHcon['__3_6_']-PAHcon['__4_5_'],color='grey',marker='.')
plt.plot([-4.5, 0.415], [1.05, 1.05], color = 'black') 
plt.plot([0.85,0.85],[4,2] , color = 'black') #[5.8] − [8.0] > 1
plt.plot([0.415,0.85],[1.05,2], color = 'black')

plt.plot([1.77,6],[1.65,1.65], color = 'black')
plt.plot([-0.3,1.77],[-1.25,1.65], color = 'black')

plt.plot([0.7,1.2],[0.7,0.7],color = 'r')
plt.plot([0.7,0.7],[1.65,0.7],color = 'r')
plt.xlabel('[4.5]-[5.8]')
plt.ylabel('[3.6]-[4.5]')
plt.xlim(-1, 3)
plt.ylim(-1.1,3.5)
plt.title('YSO')

data.remove_rows(YSO_index)
data.write('data_PASP&YSO_removed.fit')
