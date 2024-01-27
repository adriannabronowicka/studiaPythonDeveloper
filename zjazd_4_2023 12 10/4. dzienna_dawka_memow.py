import httpx
from bs4 import BeautifulSoup

response = httpx.get("https://kwejk.pl/")
with open("kwejk.html", "w") as file:
    file.write(response.text)
html = BeautifulSoup(response.text)

#html/body/main/div/div[2]/div[1]/div[1]/div/div/div[3]/figure/a/img