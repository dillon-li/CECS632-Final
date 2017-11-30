import requests
from xml.etree import ElementTree

url = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658"
response = requests.get(url)

tree = ElementTree.fromstring(response.content)
#print(tree)

for child in tree:
    #x = child.findall('info')
    #print (x)
    #if x != None:
    #    print(child.attrib)
    for anime in child:
        text = anime.itertext()
        if anime.tag == 'info':
            #print("This is info")
            att = anime.attrib
            print(att['type'])
        #print(x)
        #print(att.tag)
        #if x != None:
            #print(att.attrib)
        #for t in text:
        #    print(t)
