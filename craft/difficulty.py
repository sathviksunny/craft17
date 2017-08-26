#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:07:21 2017

@author: root
"""

import requests
from bs4 import BeautifulSoup


uda_link="https://in.udacity.com/courses/all/"
#sera_url="https://www.coursera.org/courses?languages=en&query="
#edx_url="https://www.edx.org/course?search_query="
#k=input("Enter your field? ")
#j=k.split()

'''for i in j:
	sera_url= sera_url + "+" + i
	edx_url	= edx_url + "+" + i
print(sera_url)	


r=requests.get(sera_url)
m=requests.get(edx_url)

soup1=BeautifulSoup(r.content)
soup2=BeautifulSoup(m.content)
'''
a=[]
b=[]
u=requests.get(uda_link)
soup3=BeautifulSoup(u.content)
'''
for link in soup1.find_all("a"):
	#print("<a href='%s'>%s</a>" %(link.get("href"),link.text))
	print(("%s :"+"%s")%(link.text,link.get("href")))
	
for link in soup2.find_all("a"):
	#print("<a href='%s'>%s</a>" %(link.get("href"),link.text))
	a=("%s :"+" %s"+"%s")%(link.text,"https://www.edx.org/",link.get("href"))
	print(a.strip("<").strip(">"))
'''

for span_dat in soup3.find_all("div",attrs={'class':'col-sm-4'}):
    a.append(span_dat.text.strip() )

for span_dat in soup3.find_all("div",attrs={'class':'col-sm-8'}):
    b.append(span_dat.text.strip() )
    
