from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
import requests as rq
import webbrowser as wb
import re

from requests.sessions import Request
app = FastAPI()
def htmlParse(data):
    html = rq.get(data[1:])
    f = open("test.html", "w")
    f.write(html.text)
    f.close()
    with open("test.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    findsoup = []
    stringfella = ''
    godDict = {}
    for link in soup.find_all('style'):
        content = link.string
        stringfella += content
    findsoup = (stringfella.split('{'))
    tmpl = []
    keyl = {}
    for i in findsoup:
        if '}' in i:
            temp = (i.split('}'))
            tmpl.append((temp[0].strip()).replace('\n', ''))
            tmpl.append((temp[1].strip()).replace('\n', ''))
        #tmpl.append((temp[1].strip()).replace('\n', ''))
    print(tmpl)
    tempkey = 'misc'
    keyl[tempkey] = 'THIS IS SO PYRIGHT DOESNT GET ANGY'
    for i in tmpl:
        try:
            if i[0] == '.':
                tempkey = i
            else:
                try:
                    if (keyl[tempkey]):
                        keyl[tempkey] = keyl[tempkey] + i
                except:
                    keyl[tempkey] = i
        except:
            print("GAY EXCEPTION")
    dictfella = {}
    print('\n')
    print(keyl)
    """for i in findsoup:
        text = i.strip()
        key = ''
        if (text[0] == '.'):
            key = text
        else:
            dictfella[key] = text
    print(findsoup)
    godDict['style'] = findsoup
    findsoup = []"""
    """for link in soup.find_all('p'):
        print(link.string)
        findsoup.append(link.string)
    godDict['p'] = findsoup"""
def call(data):
    if (data[0] == '$'):
        return htmlParse(data)
    else:
        results = DDGS().text(data)
        for i in range(len(results)):
            k = results[i]
            hrefs.append(k['href'])
        return{"hrefs": hrefs}
hrefs = []
@app.get("/")
async def server(data: str | None = None):
    print(data)
    return call(data)
