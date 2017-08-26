#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:07:21 2017

@author: root
"""

import requests
from bs4 import BeautifulSoup


uda_link="https://in.udacity.com/courses/all/"

a=[]
b=[]
t=[]
u=requests.get(uda_link)
soup3=BeautifulSoup(u.content)


for span_dat in soup3.find_all("div",attrs={'class':'col-sm-4'}):
    a.append(span_dat.text.strip() )

for span_dat in soup3.find_all("div",attrs={'class':'col-sm-8'}):
    b.append(span_dat.text.strip() )

import pandas as pd

df = pd.DataFrame(
    {'Title': b,
     'DIfficulty': a,
    })



