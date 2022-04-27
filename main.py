from bs4 import BeautifulSoup
import requests

url = "http://www.webscrapingfordatascience.com/postform3/"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
protection = soup.find("input", {"name":"protection"}).get("value")

data = {
    "protection":protection,
    "name":"diako",
    "gender":"M",
    "pizza":"like",
    "haircolor":"black"
}

final_result = requests.post(url, data)
print(final_result.text)