import requests
from xml.etree import ElementTree

url = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658"
response = requests.get(url)

tree = ElementTree.fromstring(response.content)
#print(tree)

for anime in tree:
    props = anime.attrib
    medium = props['type']
    print (medium)
    for info in anime:
        text = info.itertext()
        if info.tag == 'info':
            #print("This is info")
            att = info.attrib
            print(att['type'])
        #print(x)
        #print(att.tag)
        #if x != None:
            #print(att.attrib)
        #for t in text:
        #    print(t)
