from duckduckgo_search import DDGS
from fastapi import FastAPI, Request
import requests as rq
from requests.sessions import Request


app = FastAPI()
def htmlParse(data):
    html = rq.get(data[1:])
    f =  open('test.html', 'w')
    print(html, '\n \n \n')
    print(html.text)
    f.write(html.text)
        
    #parser.parse(html.text)
    

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
