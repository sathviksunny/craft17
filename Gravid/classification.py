#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:37:53 2017

@author: root
"""
import random
import pandas as pd

df_master=pd.read_csv('joined_score.csv')

df_users=pd.read_csv('user.csv')

for i in range(500):
    df_users.loc[i,'user_id']=100+i
    df_users.loc[i,'course_1']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_2']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_3']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_4']=random.sample(df_master['key'],1)[0]
    df_users.loc[i,'course_5']=random.sample(df_master['key'],1)[0]

df_users.to_csv("rand_user.csv")