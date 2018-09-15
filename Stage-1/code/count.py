# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 19:15:11 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransform

PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')
shock = Table.read('shock.fit')
PAHcon = Table.read('PAHcon.fit')
YSO = Table.read('YSO.fit')
YSOII =Table.read('YSOII.fit')

print(len(YSO))