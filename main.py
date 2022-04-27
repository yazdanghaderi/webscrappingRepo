from bs4 import BeautifulSoup
import requests

url = "http://www.webscrapingfordatascience.com/cookielogin/"


res = requests.post(url, data={"username":"dia", "password":"1234"})
# print(res.cookies)

mycookies = {
    "PHPSESSID": res.cookies["PHPSESSID"]
}

result = requests.get(url + "secret.php", cookies=mycookies)
print(result.text)