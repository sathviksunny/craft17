# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df=pd.read_csv('gravid_socre.csv')
df[['key','title','level']]=df[['key','title','level']].astype(str)

'''
print type(df['level'])

for i in df:
    if i['level'] == 'intermediate':
        df['score']=10
    if i['level'] == 'advanced':
        df['score']=20
    if i['level']=='beginner':
        df['score']=5
 '''