# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:00:50 2019

@author: Kryzha Lei Aguilar
"""

import pandas as pd

df = pd.read_csv (r'C:\Users\Kryzha Lei Aguilar\Desktop\cars.csv')

e = df.loc[df['Model']=='Camaro Z28',['Model','cyl']]
print (e)
