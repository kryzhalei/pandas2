# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:51:56 2019

@author: Kryzha Lei Aguilar
"""

import pandas as pd

df = pd.read_csv (r'C:\Users\Kryzha Lei Aguilar\Desktop\cars.csv')

d = df[df['Model']=='Mazda RX4']
print (d)
