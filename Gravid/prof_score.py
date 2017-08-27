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
df_users['cat']=0



for i in range(500):
    df_users.loc[i,'user_id']=100+i
    df_users.loc[i,'course_1']=random.choice(df_master['key'])
    df_users.loc[i,'course_2']=random.choice(df_master['key'])
    df_users.loc[i,'course_3']=random.choice(df_master['key'])
    df_users.loc[i,'course_4']=random.choice(df_master['key'])
    df_users.loc[i,'course_5']=random.choice(df_master['key'])


for i in range(500):
    score=0
    for j in range(len(df_master)):
        
        if df_users.loc[i,'course_1'] in df_master.loc[j,'key']:
                score=score+df_master.loc[j,'score']
                if df_master.loc[j,'domain']=='Android':
                    df_users.loc[i,'cat']=100+random.random() * 100
                if df_master.loc[j,'domain']=='iOS':
                    df_users.loc[i,'cat']=200+random.random() * 100
                if df_master.loc[j,'domain']=='Software Engineering':
                    df_users.loc[i,'cat']=300+random.random() * 100
                if df_master.loc[j,'domain']=='Non-Tech':
                    df_users.loc[i,'cat']=400+random.random() * 100
                if df_master.loc[j,'domain']=='Web Development':
                    df_users.loc[i,'cat']=500+random.random() * 100
                if df_master.loc[j,'domain']=='Data Science':
                    df_users.loc[i,'cat']=600+random.random() * 100
                if df_master.loc[j,'domain']=='Georgia Tech Masters in CS':
                    df_users.loc[i,'cat']=700+random.random() * 100
                
        if df_users.loc[i,'course_2'] in df_master.loc[j,'key']:
                score=score+df_master.loc[j,'score']
                if df_master.loc[j,'domain']=='Android':
                    df_users.loc[i,'cat']=100+random.random() * 100
                if df_master.loc[j,'domain']=='iOS':
                    df_users.loc[i,'cat']=200+random.random() * 100
                if df_master.loc[j,'domain']=='Software Engineering':
                    df_users.loc[i,'cat']=300+random.random() * 100
                if df_master.loc[j,'domain']=='Non-Tech':
                    df_users.loc[i,'cat']=400+random.random() * 100
                if df_master.loc[j,'domain']=='Web Development':
                    df_users.loc[i,'cat']=500
                if df_master.loc[j,'domain']=='Data Science':
                    df_users.loc[i,'cat']=600
                if df_master.loc[j,'domain']=='Georgia Tech Masters in CS':
                    df_users.loc[i,'cat']=700+random.random() * 100
                
                
        if df_users.loc[i,'course_3'] in df_master.loc[j,'key']:
                score=score+df_master.loc[j,'score']
                if df_master.loc[j,'domain']=='Android':
                    df_users.loc[i,'cat']=100+random.random() * 100+random.random() * 100+random.random() * 100
                if df_master.loc[j,'domain']=='iOS':
                    df_users.loc[i,'cat']=200+random.random() * 100
                if df_master.loc[j,'domain']=='Software Engineering':
                    df_users.loc[i,'cat']=300+random.random() * 100
                if df_master.loc[j,'domain']=='Non-Tech':
                    df_users.loc[i,'cat']=400+random.random() * 100
                if df_master.loc[j,'domain']=='Web Development':
                    df_users.loc[i,'cat']=500+random.random() * 100
                if df_master.loc[j,'domain']=='Data Science':
                    df_users.loc[i,'cat']=600+random.random() * 100
                if df_master.loc[j,'domain']=='Georgia Tech Masters in CS':
                    df_users.loc[i,'cat']=700+random.random() * 100
                
             
        if df_users.loc[i,'course_4'] in df_master.loc[j,'key']:
                score=score+df_master.loc[j,'score']
                if df_master.loc[j,'domain']=='Android':
                    df_users.loc[i,'cat']=100+random.random() * 100
                if df_master.loc[j,'domain']=='iOS':
                    df_users.loc[i,'cat']=200+random.random() * 100
                if df_master.loc[j,'domain']=='Software Engineering':
                    df_users.loc[i,'cat']=300+random.random() * 100
                if df_master.loc[j,'domain']=='Non-Tech':
                    df_users.loc[i,'cat']=400+random.random() * 100
                if df_master.loc[j,'domain']=='Web Development':
                    df_users.loc[i,'cat']=500+random.random() * 100
                if df_master.loc[j,'domain']=='Data Science':
                    df_users.loc[i,'cat']=600+random.random() * 100
                if df_master.loc[j,'domain']=='Georgia Tech Masters in CS':
                    df_users.loc[i,'cat']=700+random.random() * 100
                
             
        if df_users.loc[i,'course_5'] in df_master.loc[j,'key']:
                score=score+df_master.loc[j,'score']
                if df_master.loc[j,'domain']=='Android':
                    df_users.loc[i,'cat']=100+random.random() * 100
                if df_master.loc[j,'domain']=='iOS':
                    df_users.loc[i,'cat']=200+random.random() * 100
                if df_master.loc[j,'domain']=='Software Engineering':
                    df_users.loc[i,'cat']=300+random.random() * 100
                if df_master.loc[j,'domain']=='Non-Tech':
                    df_users.loc[i,'cat']=400+random.random() * 100
                if df_master.loc[j,'domain']=='Web Development':
                    df_users.loc[i,'cat']=500+random.random() * 100
                if df_master.loc[j,'domain']=='Data Science':
                    df_users.loc[i,'cat']=600+random.random() * 100
                if df_master.loc[j,'domain']=='Georgia Tech Masters in CS':
                    df_users.loc[i,'cat']=700+random.random() * 100
        df_users.loc[i,'score']=score
        
max1=df_users['score'].max()
for i in range(len(df_users)):
    df_users.loc[i,'score']=df_users.loc[i,'score']*100/max1+random.random()*10
df_users.to_csv("percentile.csv")
        