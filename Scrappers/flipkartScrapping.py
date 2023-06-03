import requests
from bs4 import BeautifulSoup


def flipkartScrapper(product):
    resp = requests.get("https://www.flipkart.com/search?q="+product)
    soup = BeautifulSoup(resp.content, 'html.parser')
    flipkartProducts = soup.find_all("div", {"class": "_1AtVbE"})
    productFeatures = []
    productPrices = []
    productImages = []
    productDetails = {}
    for i in flipkartProducts:

        # fetching product details
        productAnchors = i.find_all("a", {"class": "_1fQZEK"})
        for j in productAnchors:
            productfMghEO = j.find_all("div", {"class": "fMghEO"})
            for k in productfMghEO:
                lists = k.find_all("li")
                for m in lists:
                    productFeatures.append(m.text)
        productDetails["productFeatures"] = productFeatures

        # fetching product costings
        for a in productAnchors:
            divs = a.find_all("div", {"class": "_25b18c"})
            for div in divs:
                productPrices.append(div.text)
        productDetails["productPriceOffers"] = productPrices

        # fetching product images
        for img in productAnchors:
            imgList = img.find_all("img", {"loading": "eager"})
            for i in imgList:
                productImages.append(i.get("src"))
        productDetails["productImages"] = productImages

    return productDetails


