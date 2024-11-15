from bs4 import BeautifulSoup

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
    strpi = i.strip()
    try:
        if strpi[0] == '.':
            tempkey = strpi
        else:
            try:
                if (keyl[tempkey]):
                    keyl[tempkey] = keyl[tempkey] + strpi
            except:
                keyl[tempkey] = strpi
    except:
        print("GAY EXCEPTION")
dictfella = {}
print('\n')
print(keyl)
