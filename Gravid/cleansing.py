# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df=pd.read_csv('latest1.csv')

df=df.drop(df.columns[4],axis=1)
df=df.drop(df.index[135],axis=0)

df=df.dropna(axis=0,how='any')

df.to_csv("cleansed.csv")