from flask import Flask, render_template, redirect, url_for
from Scrappers import flipkartScrapping as scrap
from Scrappers import amazonScrapping as amazonScrap


app = Flask(__name__)


@app.route("/")
def home():
    productDetailsFlipkart = scrap.flipkartScrapper()
    productDetailsAmazon = amazonScrap.amazonScrapper()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
