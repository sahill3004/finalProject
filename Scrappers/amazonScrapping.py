import requests


def amazonScrapper(product):
    url = "https://amazon23.p.rapidapi.com/product-search"
    querystring = {"query": product, "page": "1", "country": "IN"}
    headers = {
        "X-RapidAPI-Key": "2368e08ca9msh71e4a6d48553d07p1fa61djsn26e5c3b1570d",
        "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
