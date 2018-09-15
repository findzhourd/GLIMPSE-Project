# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 01:47:03 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransform

data = Table.read('data_PASP&YSO_removed.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')
shock = Table.read('shock.fit')
PAHcon = Table.read('PAHcon.fit')
YSO = Table.read('YSO.fit')

sigma3 = np.sqrt(data['e__4_5_']**2-data['e__8_0_']**2)
sigma4 = np.sqrt(data['e__3_6_']**2-data['e__5_8_']**2)

x = data['__4_5_']-data['__8_0_']
y = data['__3_6_']-data['__5_8_']

YSOII_index = []

for i in range(0,len(data)):
    if x[i]-sigma3[i]>0.5:
        if y[i]-sigma4[i]>0.35:
            if y[i]+sigma4[i] <= (0.14/0.04)*(x[i]-sigma3[i]-0.5)+0.5:
                if data['__3_6_'][i]-data['__4_5_'][i]-sigma4[i]>0.15:
                    if data['e__3_6_'][i]<0.2:
                        if data['e__4_5_'][i]<0.2:
                            if data['e__5_8_'][i]<0.2:
                                if data['e__8_0_'][i]<0.2:
                                    YSOII_index.append(i)
                    
plt.figure(figsize=(10,10))

#data[YSOII_index].write('YSOII.fit')

plt.scatter(x,y)

plt.scatter(PAH1['__4_5_']-PAH1['__8_0_'],PAH1['__3_6_']-PAH1['__5_8_'],color='grey',marker='.')
plt.scatter(PAH2['__4_5_']-PAH2['__8_0_'],PAH2['__3_6_']-PAH2['__5_8_'],color='grey',marker='.')
plt.scatter(AGN['__4_5_']-AGN['__8_0_'],AGN['__3_6_']-AGN['__5_8_'],color='grey',marker='.')
plt.scatter(shock['__4_5_']-shock['__8_0_'],shock['__3_6_']-shock['__5_8_'],color='grey',marker='.')
plt.scatter(PAHcon['__4_5_']-PAHcon['__8_0_'],PAHcon['__3_6_']-PAHcon['__5_8_'],color='grey',marker='.')
plt.scatter(YSO['__4_5_']-YSO['__8_0_'],YSO['__3_6_']-YSO['__5_8_'],color='grey',marker='.')
plt.scatter(x[YSOII_index],y[YSOII_index],color='r')
plt.xlim(-2, 4)
plt.ylim(-1,4)

plt.xlabel('[4.5]-[8.0]')
plt.ylabel('[3.6]-[5.8]')

plt.title('YSO II')

data.remove_rows(YSOII_index)
data.write('phase1_final.fit')