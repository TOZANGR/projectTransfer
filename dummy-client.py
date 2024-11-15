import requests as rq
data = rq.get('http://127.0.0.1:8000', params=("data=" + input("what is your query?: ")))
data = data.json()
hrefs = data['hrefs']
print('from the following selection, which would you like to view? enter answer 0-9', hrefs)
selection = input('')
selected = hrefs[int(selection)]
html  = rq.get('http://127.0.0.1:8000', params={'data': ('$' + selected)})
print(html)
