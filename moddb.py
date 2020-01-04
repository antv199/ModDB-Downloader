import requests, urllib3, ping, socket, os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as requestURL

#modURL = str(input("Enter the ModDB mod URL or ID here: "))
modURL = "https://www.moddb.com/downloads/start/18631/all"

#disables warnings for insecure connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = requestURL(modURL)
raw_html = client.read()
parsed_html = soup(raw_html, 'html.parser')
rows = (parsed_html.findAll("div", {"class":"row"}))

#print(container)

for container in rows:
    ServerName = container.div.p.Text
    DownloadLink = "https://moddb.com" + container.div.p.a["href"]
    print(ServerName,DownloadLink)

client.close()