import requests
from bs4 import BeautifulSoup

URL = "https://lista.mercadolivre.com.br/notebook"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", class_="ui-search-result__content-wrapper")

    for product in products[:10]:  
        title = product.find("h2", class_="ui-search-item__title")
        price = product.find("span", class_="andes-money-amount__fraction")

        if title and price:
            print(f"Product: {title.text.strip()}")
            print(f"Price: R$ {price.text.strip()}")
            print("-" * 40)
else:
    print("Erro")
