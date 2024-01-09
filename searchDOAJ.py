#!/usr/bin/env python
# coding:utf-8
"""
Name : searchDOAJ.py
Author : Aurelia Vasile, MSH, UCA

Created on : 04/01/2024 12:05

"""

import csv
from methods import call_API, extract_id_Date_Title

url = 'https://doaj.org/api/search/articles/'

basic_query = 'bibjson.journal.title.exact:"Raumforschung und Raumordnung" AND bibjson.year:>=1980 AND '
abstract_search = ('bibjson.abstract:"Saxony"?pageSize=100')
keyword_search = 'bibjson.keywords:"Eastern Germany"'

# construction des url complet d'interrogation pour abstract et pour keywords
query_search_abstract = url+basic_query + abstract_search
query_search_keyword = url+basic_query + keyword_search

# appel API de DOAJ
resultatDuCallAPI = call_API(query_search_abstract)

with open('data/revue_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['doi', 'year', 'month', 'title', 'url_article', 'keywords', 'affiliations', 'id_article']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    extract_id_Date_Title(resultatDuCallAPI, writer, fieldnames)