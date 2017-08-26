#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 02:37:53 2017

@author: root
"""
import random
import pandas as pd

df_master=pd.read_csv('joined_score.csv')

df_users=pd.read_csv('user.csv')


df_users['score']=0



for i in range(100):
    df_users.loc[i,'user_id']=100+i
    df_users.loc[i,'course_1']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_2']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_3']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_4']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_5']=random.sample(df_master['key'],1)[0]

for i in range(100):
    score=0
    for j in range(len(df_master)):
        
        if df_users.loc[i,'course_1'] in df_master['key'][j]:
                score=score+df_master.loc[i,'score']

        if df_users.loc[i,'course_2'] in df_master['key'][j]:
                score=score+df_master.loc[i,'score']
                
        if df_users.loc[i,'course_3'] in df_master['key'][j]:
                score=score+df_master.loc[i,'score']
             
        if df_users.loc[i,'course_4'] in df_master['key'][j]:
                score=score+df_master.loc[i,'score']
             
        if df_users.loc[i,'course_5'] in df_master['key'][j]:
                score=score+df_master.loc[i,'score']

    df_users.loc[i,'score']=score
max1=df_users['score'].max()
for i in range(len(df_users)):
    df_users.loc[i,'score']=df_users.loc[i,'score']*100/max1
df_users.to_csv("percentile.csv")
        