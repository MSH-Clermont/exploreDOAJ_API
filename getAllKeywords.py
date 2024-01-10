#!/usr/bin/env python
# coding:utf-8
"""
Name : getAllKeywords.py
Author : Aurelia Vasile, MSH, UCA

Created on : 10/01/2024 15:37

"""


import csv
from methods import call_API, extractKeywordsByYear

url = 'https://doaj.org/api/search/articles/'

basic_query = 'bibjson.journal.title.exact:"Raumforschung und Raumordnung" AND bibjson.year:>=2008?pageSize=100'
query_allKeywords = url+ basic_query
# appel API de DOAJ
resultatDuCallAPI = call_API(query_allKeywords)

with open('data/allKeywords.csv', 'w', newline='') as csvfile:
    fieldnames = ['keyword', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    extractKeywordsByYear(resultatDuCallAPI, writer, fieldnames)