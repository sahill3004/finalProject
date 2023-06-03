from flask import Flask, render_template, request, url_for
from Scrappers import flipkartScrapping as flipkartScrap
from Scrappers import amazonScrapping as amazonScrap

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/compare/products", methods=['POST'])
def compareProducts():
    product = request.form.get("product")
    flipkart = flipkartScrap.flipkartScrapper(product)
    amazon = amazonScrap.amazonScrapper(product)
    # print(flipkartProducts)
    # print(amazonProducts)
    flipkartProducts = flipkart
    print(flipkartProducts)
    amazonProducts = amazon.get("result")
    # print(amazonProducts)
    return render_template("compare.html", flipkartProducts=[1, 2, 3], amazonProducts=amazonProducts)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False)
