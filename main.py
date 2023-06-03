from flask import Flask, render_template, redirect, url_for
from Scrappers import flipkartScrapping as scrap


app = Flask(__name__)


@app.route("/")
def home():
    productDetails = scrap.flipkartScrapper("dell")
    print(productDetails)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
