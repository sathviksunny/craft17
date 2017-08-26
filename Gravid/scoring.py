# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df=pd.read_csv('cleansed.csv')
df['score']=0

for i in range(len(df)):
    if df.loc[i,"level"]=='beginner':
        df.loc[i,'score']=5
    if df.loc[i,"level"]=='intermediate':
        df.loc[i,'score']=10
    if df.loc[i,"level"]=='advanced':
        df.loc[i,'score']=20
df=df.drop(df.columns[0],axis=1)
df.to_csv('scored.csv')