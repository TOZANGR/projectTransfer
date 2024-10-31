import requests
url = 'https://loger-ochre.vercel.app/api/ToServe.js'
resp = requests.post(url)
print(resp.json())