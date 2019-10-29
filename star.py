import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36',
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"}


url = "http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html"
response = requests.get(url, headers=headers) # для обхода на проверку бота (чтобы он возвращал 200 запрос)

html = response.text
soup = BeautifulSoup(html, "html.parser")
conteiner = soup.find("div", {"class": "td-post-content"})
elements = conteiner.find_all("p")

string = "Топ-10 самых больших звезд во Вселенной: \n"

for element in elements:
    if element.find("strong"):
        string += "\t" + element.strong.text + "\n"

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(string)
