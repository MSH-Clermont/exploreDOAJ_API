#!/usr/bin/env python
# coding:utf-8
"""
Name : methods.py
Author : Aurelia Vasile, MSH, UCA

Created on : 05/01/2024 09:59

"""
import requests

payload = {}
headers = {}
def call_API(url):
    global response, resultat
    response = requests.request("GET", url, headers=headers, data=payload)
    resultat = response.json()
    return resultat

def extract_id_Date_Title(resultatDuCallAPI, writer, fieldnames):
    if "results" in resultatDuCallAPI:
        if resultatDuCallAPI['results']:
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
                keywords=['mots clés manquants']
                if "keywords" in eachResult["bibjson"]:
                    keywords = eachResult["bibjson"]["keywords"]
                affiliation = ""
                for eachAuthor in eachResult["bibjson"]["author"]:
                    if "affiliation" in eachAuthor:
                        affiliation += eachAuthor["affiliation"] + " | "
                id_article = eachResult["id"]

                writer.writerow(
                    {fieldnames[0]: doi,
                     fieldnames[1]: month,
                     fieldnames[2]: year,
                     fieldnames[3]: title,
                     fieldnames[4]: url,
                     fieldnames[5]: keywords,
                     fieldnames[6]: affiliation,
                     fieldnames[7]: id_article
                     })

            if "next" in resultatDuCallAPI:
                nextResultat = call_API(resultatDuCallAPI["next"])
                extract_id_Date_Title(nextResultat, writer, fieldnames)
        else:
            print("il n'y a aucun résultat")
    else:
        print("requete incorrecte")