# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:06:41 2019

@author: Kryzha Lei Aguilar
"""

import pandas as pd

df = pd.read_csv (r'C:\Users\Kryzha Lei Aguilar\Desktop\cars.csv')

f = df.loc[(df['Model']=='Mazda RX4 Wag')|(df['Model']=='Honda Civic')|(df['Model']=='Ford Pantera L'),['Model','cyl','gear']]
print (f)
