from flask import Flask, render_template, redirect, url_for
from Scrappers import flipkartScrapping as scrap
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


@app.route("/compare")
def compare():
    return render_template("compare.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False)
