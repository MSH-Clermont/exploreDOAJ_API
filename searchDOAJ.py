#!/usr/bin/env python
# coding:utf-8
"""
Name : searchDOAJ.py
Author : Aurelia Vasile, MSH, UCA

Created on : 04/01/2024 12:05

"""

import requests
import csv

url = 'https://doaj.org/api/search/articles/'
basic_query = 'bibjson.journal.title.exact:\"Raumforschung und Raumordnung\" AND bibjson.year:>=2000 AND '
abstract_search = 'bibjson.abstract:\"Germany\"?pageSize=10'
payload = {}
headers = {}
query_search = url+basic_query + abstract_search

def call_API(url):
    global response, resultat
    response = requests.request("GET", url, headers=headers, data=payload)
    resultat = response.json()
    return resultat

def extract_id_Date_Title(resultatDuCallAPI):
    for eachResult in resultatDuCallAPI['results']:
        doi = "https://doi.org/"
        for identifiant in eachResult["bibjson"]["identifier"]:
            if identifiant["type"] == "doi":
                doi = doi + identifiant["id"]
                break
        url=''
        for lien in eachResult["bibjson"]["link"]:
            if lien["type"]== "fulltext":
                url= url+lien["url"]

        month = eachResult["bibjson"]["month"]
        year = eachResult["bibjson"]["year"]
        title = eachResult["bibjson"]["title"]
        writer.writerow(
            {fieldnames[0]: doi,
             fieldnames[1]: month,
             fieldnames[2]: year,
             fieldnames[3]: title,
             fieldnames[4]: url
             })
    if resultatDuCallAPI["next"]:
        nextResultat = call_API(resultatDuCallAPI["next"])
        extract_id_Date_Title(nextResultat)

resultatDuCallAPI = call_API(query_search)

with open('data/revue_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['id_article_doi', 'year', 'month', 'title', 'url_article']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    extract_id_Date_Title(resultatDuCallAPI)