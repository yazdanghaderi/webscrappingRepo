import requests
from bs4 import BeautifulSoup
import re
url ="https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

table = soup.find('table',class_="wikitable plainrowheaders wikiepisodetable")
episods = []
# for table in epTable:
headers = []
for header in table.find("tr").findAll("th"):
    headers.append(header.text)

for row in table.findAll("tr")[1:]:
    values = []
    for col in row.findAll(["th","td"]):
        values.append(col.text)
    if values:
        episodDict = {headers[i]:values[i] for i in range(len(values))}
        episods.append(episodDict)
print(episods)
# for ep in episods:
#     print(ep)








