import httpx
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://pcshop.ge/product-category/notebooks/"

products = []

def page_link(page_num: int) -> str:
    return f"{BASE_URL}?_paged={page_num}"

response = httpx.get(page_link(1))

soup = BeautifulSoup(response.text, "html.parser")

pages = soup.find_all("a", class_="page-numbers")
pages = [page for page in pages if page.text.isdigit()]
last_page = int(pages[-1].text)

for page in range(1, last_page):

    print(page)
    for product_elem in soup.find_all("div", class_="product-item__inner"):
        title = product_elem.find("h2", class_="woocommerce-loop-product__title").text
        price = product_elem.find("span", class_="price").text
        product_link = product_elem.find("a", class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")["href"]
        original_price = price
        if price.count("₾") > 1:
            price_text = price
            price = price_text.split("₾")[1].strip()
            original_price = price_text.split("₾")[2].strip()

        print(title, price, original_price, product_link, sep=" | ")
        products.append({"title": title, "price": price, "original_price": original_price, "link": product_link})
    response = httpx.get(page_link(page + 1))
    soup = BeautifulSoup(response.text, "html.parser")

df = pd.DataFrame.from_records(products)
df.to_excel("products.xlsx", index=False)