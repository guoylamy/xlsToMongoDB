# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:22:22 2023

@author: Yilin
"""

import pandas as pd
from pymongo import MongoClient

options = ["Computer and Information Systems Managers", "Computer and Information Analysts", "Computer Systems Analysts", "Computer and Information Research Scientists",
           "Computer Support Specialists", "Computer Network Support Specialists", "Software and Web Developers, Programmers, and Testers",
           "Computer Programmers", "Software Developers", "Software Quality Assurance Analysts and Testers", "Web Developers",
           "Web and Digital Interface Designers", "Data Scientists"]

df = pd.read_excel("D:/File/job/Astoria.AI/oesm17all/oesm17all/all_data_M_2017.xlsx")
df = df.loc[df['OCC_TITLE'].isin(options)]
df = df.loc[df['AREA_TYPE'] != 6]
print(df.shape)

mongodburi = "mongodb+srv://veet123:veet123@indeedcluster.eci7aym.mongodb.net"
mongo_client = MongoClient(mongodburi) 
db=mongo_client.Wage

header= ["AREA", "AREA_TITLE", "AREA_TYPE", "NAICS", "NAICS_TITLE", "I_GROUP", "OWN_CODE", "OCC_CODE", "OCC_TITLE",
          "O_GROUP", "TOT_EMP", "EMP_PRSE", "H_MEAN", "A_MEAN", "MEAN_PRSE", "H_PCT10", "H_PCT25", "H_MEDIAN", "H_PCT75", "H_PCT90", 
          "A_PCT10", "A_PCT25", "A_MEDIAN", "A_PCT75", "A_PCT90", "ANNUAL", "HOURLY"]


for index, row in df.iterrows():
    data={}
    for field in header:
        data[field]=row[field]
    
    data['Year'] = 2017
    data['Month'] = 5
    db.all.insert_one(data)