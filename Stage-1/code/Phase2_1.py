# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 02:59:16 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransform

data = Table.read('phase1_final.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')
shock = Table.read('shock.fit')
PAHcon = Table.read('PAHcon.fit')
YSO = Table.read('YSO.fit')

data['__5_8_'].fill_value=0
print(data.colnames)
bb=0
for i in range (100,400):
    if np.isnan(data['__5_8_'][i])==True:
        bb=bb+1
print(bb)


c = 5.4478

HKm = data['Hmag']-data['Ksmag']
_36_45_m = data['__3_6_']-data['__4_5_']
K36m = data['Ksmag']-data['__3_6_']

HK0 = (1.33*(c*HKm - _36_45_m)-0.133)/(1.33*c-1)

_36_45_0 = _36_45_m - (HKm - HK0)*c
K36_0 = K36m-(HKm-HK0)*0.671
_36_0 = data['__3_6_']

sigma1 = np.sqrt(data['e__3_6_']**2-data['e__4_5_']**2)
sigma2 = np.sqrt(data['e_Ksmag']**2-data['e__3_6_']**2)

YSO3_index = []
proto_index = []

for i in range(0,len(data)):
    if np.isnan(data['__5_8_'][i])==True:
        if _36_45_0[i] - sigma1[i] > 0.101:
            if K36_0[i] - sigma2[i] > 0:
                if K36_0[i]-sigma2[i] > -2.85714*(_36_45_0[i]-sigma1[i]-0.101)+0.5:
                    if data['e_Hmag'][i]<0.1:
                        if data['e_Ksmag'][i]<0.1:
                            if data['e_Jmag'][i]<0.1:
                                if K36_0[i]-sigma2[i] > -2.85714*(_36_45_0[i]-sigma1[i]-0.401)+1.7:
                                    if data['__3_6_'][i]<15:
                                        proto_index.append(i)
                                elif data['__3_6_'][i]<14.5:
                                    YSO3_index.append(i)
    elif np.isnan(data['__8_0_'][i])==True:
        if _36_45_0[i] - sigma1[i] > 0.101:
            if K36_0[i] - sigma2[i] > 0:
                if K36_0[i]-sigma2[i] > -2.85714*(_36_45_0[i]-sigma1[i]-0.101)+0.5:
                    if data['e_Hmag'][i]<0.1:
                        if data['e_Ksmag'][i]<0.1:
                            if data['e_Jmag'][i]<0.1:
                                if K36_0[i]-sigma2[i] > -2.85714*(_36_45_0[i]-sigma1[i]-0.401)+1.7:
                                    if data['__3_6_'][i]<15:
                                           proto_index.append(i)
                                elif data['__3_6_'][i]<14.5:
                                    YSO3_index.append(i)
plt.figure(figsize=(10,10))
print(len(proto_index))
print(len(YSO3_index))
#data[YSOII_index].write('YSOII.fit')

plt.scatter(_36_45_0,K36_0)


plt.scatter(_36_45_0[YSO3_index],K36_0[YSO3_index],color='b')
plt.scatter(_36_45_0[proto_index],K36_0[proto_index],color='r')

plt.xlabel('$[[3.6]-[4.5]_0]$')
plt.ylabel('$[K-[3.6]]_0$')
plt.xlim(-4,7)
plt.ylim(-1.5,5)
plt.title('Phase 2 classification')
data.remove_rows(YSO3_index)
data.write('data_phase2.fit')
#data[YSO3_index].write('YSO3.fit')
#data[proto_index].write('proto.fit')