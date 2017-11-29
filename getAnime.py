import requests
from xml.etree import ElementTree

url = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658"
response = requests.get(url)

tree = ElementTree.fromstring(response.content)

for child in tree[0]:
    text = child.itertext()
    for t in text:
        print(t)
