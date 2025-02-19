import requests
from bs4 import BeautifulSoup
import csv  # Importamos a biblioteca para manipular CSV


URL = "https://lista.mercadolivre.com.br/notebook"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


response = requests.get(URL, headers=HEADERS)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", class_="ui-search-result__content-wrapper")

    
    with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.writer(arquivo_csv)  
        writer.writerow(["Produto", "Preço"])  

        for product in products[:10]:  
            title = product.find("h2", class_="ui-search-item__title")
            price = product.find("span", class_="andes-money-amount__fraction")

            if title and price:
                prod_name = title.text.strip()
                prod_price = price.text.strip()
                writer.writerow([prod_name, prod_price]) 

                print(f"Produto: {prod_name}")
                print(f"Preço: R$ {prod_price}")
                print("-" * 40)

    print("Os dados foram salvos no arquivo produtos.csv!")
else:
    print("Error")
