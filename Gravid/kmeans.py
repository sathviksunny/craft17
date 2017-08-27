#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 03:25:02 2017

@author: root
"""
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

df=pd.read_csv('percentile.csv')
a=[]
b=[]
x=[]

import matplotlib.pyplot as plt


score=df['score'].tolist()
cat=df['cat'].tolist()

#lst=np.array(score,cat);
for i in range(0,len(score)):
    x.append((score[i],cat[i]))
x=np.array(x)
plt.scatter(score,cat)

#print x

kmeans = KMeans(n_clusters=len(df)/5, random_state=0)
idx=kmeans.fit_predict(x)
centroids=kmeans.cluster_centers_

print(centroids)
cluster_map=dict(zip(x,idx))
print cluster_map


plt.scatter(idx)
print kmeans.labels_


print kmeans.predict(x)

#o= kmeans.cluster_centers_