import requests, urllib3, socket, os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as requestURL

#modURL = str(input("Enter the ModDB mod URL or ID here: "))
modURL = "https://www.moddb.com/downloads/start/18631/all"
servers =[]
downloadNums=[]
#disables warnings for insecure connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = requestURL(modURL)
raw_html = client.read()
parsed_html = soup(raw_html, 'html.parser')
rows = (parsed_html.findAll("div", {"class":"row"}))
downloads = soup.find_all('span', {'class' : 'subheading'})

print(rows)

for container in rows:
    DownloadLink = "https://moddb.com" + container.div.p.a["href"]
    servers.append(DownloadLink)
    print(DownloadLink)

for download in downloads:
    downloadNums.append(download.Text)
    print(download)

client.close()