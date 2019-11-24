# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:24:59 2019

@author: Kryzha Lei Aguilar
"""

import pandas as pd

df = pd.read_csv (r'C:\Users\Kryzha Lei Aguilar\Desktop\cars.csv')

c = df.iloc[0:5,1:12:2]
print (c)