from bs4 import BeautifulSoup
import cssutils
class swag:
    def __init__(self, key, style, tor):
        self.key = key
        self.body = style
        self.type = tor
    def config(self, styleType, parents):
        self.attrs = self.type
        self.tag = self.key
        self.styleType = styleType
        self.parents = parents

def typeDefs(key):

    if key[0] == '.':
        typeOfRule = 'class'
    elif key[0] == '#':
        typeOfRule = 'id'
    elif key[0] == '*':
        typeOfRule = 'all'
    else:
        if ('.' in key):
            typeOfRule = 'tag_property'
        elif (':' in key):
            typeOfRule = 'tag_psudo-class_or_media'
        else:
            typeOfRule = 'tag'
    return(typeOfRule)

def styleObjs(data):
    swags = []
    l = []
    for rule in data.cssRules:
        try:
            key = rule.selectorText
        except:
            key = getattr(rule.media, ((((str(rule.typeString)).split('_'))[0]).lower()) + 'Text')
        try:
            style = rule.style
        except:
            style = key
        typeOfRule = []
        if ',' in key:
            for i in key.split(','):
                typeOfRule.append(typeDefs(i))
        else:
            typeOfRule.append(typeDefs(key))

        
        swags.append(swag(key, style, typeOfRule))
    
    return [swags]

def startPsuedo(style, html):
    masterList = []
    masterList.append('int main (int argc, char **argv){\n')
    id = 0
    for obj in html:
        if obj.tag == 'button':
            masterList.append(f'GtkWidget *button{id};\n')
        elif obj.tag == 'p':
            masterList.append(f'GtkWidget *text{id};\n')
        elif obj.tag == 'a':
            masterList.append(f'GtkWidget *atext{id};\n')
        elif obj.tag == 'h1':
            masterList.append(f'GtkWidget *h1text{id};\n')
        else:
            masterList.append(f'GtkWidget *divtext{id};\n')
        id += 1
    masterList.append('}')


    with open('render.cpp', 'w') as file:
        file.writelines(masterList)

def htmlObjs(data):
    bodyParsed = []
    print(len(data))
    data = data.find_all()
    print(len(data))

    for link in data:
        templ = []

        line = link
        if line.name:
            temp = swag(line.name, line.string, line.attrs)
            try:
                link.attrs['id']
                templ.append('id')
            except AttributeError:
                link.attrs['class']
                templ.append('class')
            except:
                templ.append('tag')
            t = line
            parentl = []
            while t.parent and t.parent.name != 'body':
                t = t.parent
                parentl.append(t.name)
            temp.config(templ, parentl)
            bodyParsed.append(temp)
    return(bodyParsed)
def parse():

    with open("test.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    #soup = BeautifulSoup(soup, 'html.parser')
    sill = ['style']
    #parses css and stylesheet into usable data for future processes
    stringfella = ''
    for link in soup.find_all(sill):
        content = link.string
        if (content):
            stringfella += content
    parsed = cssutils.parseString(stringfella)
    style = styleObjs(parsed)
    html = htmlObjs(soup.body)
    startPsuedo(style, html)

parse()