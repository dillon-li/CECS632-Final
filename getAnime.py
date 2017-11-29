import requests

url = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658"
response = requests.get(url)

print(response.content);
