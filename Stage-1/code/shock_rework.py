# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:15:27 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms

data = Table.read('data_PAH&AGN_removed.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')


x = data['__4_5_']-data['__5_8_']
y = data['__3_6_']-data['__4_5_']

shock_index = []
for i in range(0,len(data)):
    if y[i]>((1.2/0.55)*(x[i]-0.3)+0.8):
        if x[i]<=0.95:
            if y[i]>1.05:
                if data['e__3_6_'][i]<0.2:
                    if data['e__4_5_'][i]<0.2:
                        if data['e__5_8_'][i]<0.2:
                            if data['e__8_0_'][i]<0.2:
                                shock_index.append(i)
         
shock = data[shock_index]
#shock.write('shock.fit')

plt.figure(figsize=(10,10))
plt.scatter(x,y)
plt.scatter(x[shock_index],y[shock_index], color = 'b')
plt.scatter(PAH1['__4_5_']-PAH1['__5_8_'],PAH1['__3_6_']-PAH1['__4_5_'],color='black',marker='.')
plt.scatter(PAH2['__4_5_']-PAH2['__8_0_'],PAH2['__3_6_']-PAH2['__4_5_'],color='black',marker='.')
plt.scatter(AGN['__4_5_']-AGN['__5_8_'],AGN['__3_6_']-AGN['__4_5_'],color='black',marker='.')



plt.xlabel('[4.5]-[5.8]')
plt.ylabel('[3.6]-[4.5]')
plt.xlim(-0.8, 2.8)
plt.ylim(-1,3.4)
plt.title('shock')

data.remove_rows(shock_index)
data.write('data_PAH&AGN&shock_removed.fit')
